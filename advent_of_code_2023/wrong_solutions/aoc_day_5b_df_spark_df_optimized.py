from utils import parse_text_file_by_line
import pandas as pd
import numpy as np
from pyspark.sql.functions import *
from pyspark.sql.functions import min as _min
from pyspark.sql import DataFrame, SparkSession
from functools import reduce
import pyspark
from pyspark.sql.window import Window


def extract_maps(input_text):
    spark = SparkSession.builder.appName('aoc').getOrCreate()
    particular_value = ''
    split_list = []
    temp_list = []
    for i in input_text:
        if i == particular_value:
            split_list.append(temp_list)
            temp_list = []
        else:
            temp_list.append(i)
    split_list.append(temp_list)

    # Seeds
    seeds = split_list[0][0].split('seeds: ')[1].split(' ')
    seeds = [int(i) for i in seeds]
    seeds_final = []
    for i in range(int(len(seeds) / 2)):
        seeds_final.append([seeds[i*2], seeds[i] + seeds[i+1]])

    seed_df_list = []
    for single_seed_range in seeds_final:
        df = spark.range(start=single_seed_range[0], end=single_seed_range[1]).withColumnRenamed("id", "seed")
        seed_df_list.append(df)
    seeds_df = reduce(DataFrame.unionByName, seed_df_list)
    #print('seeds_df.count() 1: ', seeds_df.count())

    # Seed-to-Soil
    seed_to_soil_raw = split_list[1][1:]
    seed_to_soil_map = [i.split(' ') for i in seed_to_soil_raw]
    seed_to_soil_map = [[int(j) for j in i] for i in seed_to_soil_map]

    seed_to_soil_df_list = []
    for single_seed_to_soil_map in seed_to_soil_map:
        df_1 = spark.range(single_seed_to_soil_map[0], single_seed_to_soil_map[0] + single_seed_to_soil_map[2]).withColumnRenamed("id",
                                                                                                              "soil")
        windowSpec = Window.partitionBy().orderBy(col('soil').asc())
        df_1 = df_1.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_2 = spark.range(single_seed_to_soil_map[1], single_seed_to_soil_map[1] + single_seed_to_soil_map[2]).withColumnRenamed("id", "seed")
        windowSpec = Window.partitionBy().orderBy(col('seed').asc())
        df_2 = df_2.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_1 = df_1.join(df_2, on=['col_id'], how="inner").drop('col_id')
        seed_to_soil_df_list.append(df_1
                                    )
    seed_to_soil_df = reduce(DataFrame.union, seed_to_soil_df_list)

    seeds_df = seeds_df.join(seed_to_soil_df, on=["seed"],how="left")
    seeds_df = seeds_df.withColumn("soil", when(col("soil").isNull(), col("seed")).otherwise(col("soil")))
    seeds_df = seeds_df.drop('seed')
    #print('seeds_df.count() 2: ', seeds_df.count())

    # Soil-to-Fertilizer
    soil_to_fertilizer_raw = split_list[2][1:]
    soil_to_fertilizer_map = [i.split(' ') for i in soil_to_fertilizer_raw]
    soil_to_fertilizer_map = [[int(j) for j in i] for i in soil_to_fertilizer_map]

    soil_to_fertilizer_df_list = []
    for single_soil_to_fertilizer_map in soil_to_fertilizer_map:
        df_1 = spark.range(single_soil_to_fertilizer_map[0],
                           single_soil_to_fertilizer_map[0] + single_soil_to_fertilizer_map[2]).withColumnRenamed("id",
                                                                                                      "fertilizer")
        windowSpec = Window.partitionBy().orderBy(col('fertilizer').asc())
        df_1 = df_1.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_2 = spark.range(single_soil_to_fertilizer_map[1],
                           single_soil_to_fertilizer_map[1] + single_soil_to_fertilizer_map[2]).withColumnRenamed("id", "soil")
        windowSpec = Window.partitionBy().orderBy(col('soil').asc())
        df_2 = df_2.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_1 = df_1.join(df_2, on=['col_id'], how="inner").drop('col_id')
        soil_to_fertilizer_df_list.append(df_1
                                    )
    soil_to_fertilizer_df = reduce(DataFrame.union, soil_to_fertilizer_df_list)

    seeds_df = seeds_df.join(soil_to_fertilizer_df, on=["soil"], how="left")
    seeds_df = seeds_df.withColumn("fertilizer", when(col("fertilizer").isNull(), col("soil")).otherwise(col("fertilizer")))
    seeds_df = seeds_df.drop('soil')
    #print('seeds_df.count() 3: ', seeds_df.count())


    # Fertilizer-to-Water
    fertilizer_to_water_raw = split_list[3][1:]
    fertilizer_to_water_map = [i.split(' ') for i in fertilizer_to_water_raw]
    fertilizer_to_water_map = [[int(j) for j in i] for i in fertilizer_to_water_map]

    fertilizer_to_water_df_list = []
    for single_fertilizer_to_water_map in fertilizer_to_water_map:
        df_1 = spark.range(single_fertilizer_to_water_map[0],
                           single_fertilizer_to_water_map[0] + single_fertilizer_to_water_map[2]).withColumnRenamed("id",
                                                                                                                  "water")
        windowSpec = Window.partitionBy().orderBy(col('water').asc())
        df_1 = df_1.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_2 = spark.range(single_fertilizer_to_water_map[1],
                           single_fertilizer_to_water_map[1] + single_fertilizer_to_water_map[2]).withColumnRenamed("id",
                                                                                                                  "fertilizer")
        windowSpec = Window.partitionBy().orderBy(col('fertilizer').asc())
        df_2 = df_2.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_1 = df_1.join(df_2, on=['col_id'], how="inner").drop('col_id')
        fertilizer_to_water_df_list.append(df_1
                                          )
    fertilizer_to_water_df = reduce(DataFrame.union, fertilizer_to_water_df_list)

    seeds_df = seeds_df.join(fertilizer_to_water_df, on=["fertilizer"], how="left")
    seeds_df = seeds_df.withColumn("water",
                                   when(col("water").isNull(), col("fertilizer")).otherwise(col("water")))
    seeds_df = seeds_df.drop('fertilizer')
    #print('seeds_df.count() 4: ', seeds_df.count())

    # Water-to-Light
    water_to_light_raw = split_list[4][1:]
    water_to_light_map = [i.split(' ') for i in water_to_light_raw]
    water_to_light_map = [[int(j) for j in i] for i in water_to_light_map]

    water_to_light_df_list = []
    for single_water_to_light_map in water_to_light_map:
        df_1 = spark.range(single_water_to_light_map[0],
                           single_water_to_light_map[0] + single_water_to_light_map[2]).withColumnRenamed(
            "id",
            "light")
        windowSpec = Window.partitionBy().orderBy(col('light').asc())
        df_1 = df_1.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_2 = spark.range(single_water_to_light_map[1],
                           single_water_to_light_map[1] + single_water_to_light_map[2]).withColumnRenamed(
            "id",
            "water")
        windowSpec = Window.partitionBy().orderBy(col('water').asc())
        df_2 = df_2.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_1 = df_1.join(df_2, on=['col_id'], how="inner").drop('col_id')
        water_to_light_df_list.append(df_1
                                           )
    water_to_light_df = reduce(DataFrame.union, water_to_light_df_list)

    seeds_df = seeds_df.join(water_to_light_df, on=["water"], how="left")
    seeds_df = seeds_df.withColumn("light",
                                   when(col("light").isNull(), col("water")).otherwise(col("light")))
    #print('seeds_df.count() 4: ', seeds_df.count())
    seeds_df = seeds_df.drop('water')

    # Light-to-Temperature
    light_to_temperature_raw = split_list[5][1:]
    light_to_temperature_map = [i.split(' ') for i in light_to_temperature_raw]
    light_to_temperature_map = [[int(j) for j in i] for i in light_to_temperature_map]

    light_to_temperature_df_list = []
    for single_light_to_temperature_map in light_to_temperature_map:
        df_1 = spark.range(single_light_to_temperature_map[0],
                           single_light_to_temperature_map[0] + single_light_to_temperature_map[2]).withColumnRenamed(
            "id",
            "temperature")
        windowSpec = Window.partitionBy().orderBy(col('temperature').asc())
        df_1 = df_1.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_2 = spark.range(single_light_to_temperature_map[1],
                           single_light_to_temperature_map[1] + single_light_to_temperature_map[2]).withColumnRenamed(
            "id",
            "light")
        windowSpec = Window.partitionBy().orderBy(col('light').asc())
        df_2 = df_2.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_1 = df_1.join(df_2, on=['col_id'], how="inner").drop('col_id')
        light_to_temperature_df_list.append(df_1
                                      )
    light_to_temperature_df = reduce(DataFrame.union, light_to_temperature_df_list)

    seeds_df = seeds_df.join(light_to_temperature_df, on=["light"], how="left")
    seeds_df = seeds_df.withColumn("temperature",
                                   when(col("temperature").isNull(), col("light")).otherwise(col("temperature")))
    seeds_df = seeds_df.drop('light')
    #print('seeds_df.count() 5: ', seeds_df.count())

    # Temperature-to-Humidity
    temperature_to_humidity_raw = split_list[6][1:]
    temperature_to_humidity_map = [i.split(' ') for i in temperature_to_humidity_raw]
    temperature_to_humidity_map = [[int(j) for j in i] for i in temperature_to_humidity_map]

    temperature_to_humidity_df_list = []
    for single_temperature_to_humidity_map in temperature_to_humidity_map:
        df_1 = spark.range(single_temperature_to_humidity_map[0],
                           single_temperature_to_humidity_map[0] + single_temperature_to_humidity_map[2]).withColumnRenamed(
            "id",
            "humidity")
        windowSpec = Window.partitionBy().orderBy(col('humidity').asc())
        df_1 = df_1.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_2 = spark.range(single_temperature_to_humidity_map[1],
                           single_temperature_to_humidity_map[1] + single_temperature_to_humidity_map[2]).withColumnRenamed(
            "id",
            "temperature")
        windowSpec = Window.partitionBy().orderBy(col('temperature').asc())
        df_2 = df_2.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_1 = df_1.join(df_2, on=['col_id'], how="inner").drop('col_id')
        temperature_to_humidity_df_list.append(df_1
                                            )
    temperature_to_humidity_df = reduce(DataFrame.union, temperature_to_humidity_df_list)

    seeds_df = seeds_df.join(temperature_to_humidity_df, on=["temperature"], how="left")
    seeds_df = seeds_df.withColumn("humidity",
                                   when(col("humidity").isNull(), col("temperature")).otherwise(col("humidity")))
    #print('seeds_df.count() 6: ', seeds_df.count())
    seeds_df = seeds_df.drop('temperature')


    # Humidity-to-Location
    humidity_to_location_raw = split_list[7][1:]
    humidity_to_location_map = [i.split(' ') for i in humidity_to_location_raw]
    humidity_to_location_map = [[int(j) for j in i] for i in humidity_to_location_map]

    humidity_to_location_df_list = []
    for single_humidity_to_location_map in humidity_to_location_map:
        df_1 = spark.range(single_humidity_to_location_map[0],
                           single_humidity_to_location_map[0] + single_humidity_to_location_map[
                               2]).withColumnRenamed(
            "id",
            "location")
        windowSpec = Window.partitionBy().orderBy(col('location').asc())
        df_1 = df_1.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_2 = spark.range(single_humidity_to_location_map[1],
                           single_humidity_to_location_map[1] + single_humidity_to_location_map[
                               2]).withColumnRenamed(
            "id",
            "humidity")
        windowSpec = Window.partitionBy().orderBy(col('humidity').asc())
        df_2 = df_2.withColumn(
            'col_id',
            row_number().over(windowSpec)
        )
        df_1 = df_1.join(df_2, on=['col_id'], how="inner").drop('col_id')
        humidity_to_location_df_list.append(df_1
                                               )
    humidity_to_location_df = reduce(DataFrame.union, humidity_to_location_df_list)

    seeds_df = seeds_df.join(humidity_to_location_df, on=["humidity"], how="left")
    seeds_df = seeds_df.withColumn("location",
                                   when(col("location").isNull(), col("humidity")).otherwise(col("location")))
    #print('seeds_df.count() 7: ', seeds_df.count())
    seeds_df = seeds_df.drop('humidity')

    array = seeds_df.toPandas().to_numpy()
    print(np.min(array))


def aoc_day_5a(input_text):
    extract_maps(input_text)


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../input/aoc_day_5_test_input.txt")
    aoc_day_5a(parsed_file)

    # parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_5_actual_input.txt")
    # aoc_day_5a(parsed_file)
#


from utils import parse_text_file_by_line


def extract_maps(input_text):
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


    seeds = split_list[0][0].split('seeds: ')[1].split(' ')
    seeds = [int(i) for i in seeds]

    seed_to_soil_raw = split_list[1][1:]
    seed_to_soil_map = [i.split(' ') for i in seed_to_soil_raw]
    seed_to_soil_map = [[int(j) for j in i] for i in seed_to_soil_map]

    soil_to_fertilizer_raw = split_list[2][1:]
    soil_to_fertilizer_map = [i.split(' ') for i in soil_to_fertilizer_raw]
    soil_to_fertilizer_map = [[int(j) for j in i] for i in soil_to_fertilizer_map]

    fertilizer_to_water_raw = split_list[3][1:]
    fertilizer_to_water_map = [i.split(' ') for i in fertilizer_to_water_raw]
    fertilizer_to_water_map = [[int(j) for j in i] for i in fertilizer_to_water_map]

    water_to_light_raw = split_list[4][1:]
    water_to_light_map = [i.split(' ') for i in water_to_light_raw]
    water_to_light_map = [[int(j) for j in i] for i in water_to_light_map]

    light_to_temperature_raw = split_list[5][1:]
    light_to_temperature_map = [i.split(' ') for i in light_to_temperature_raw]
    light_to_temperature_map = [[int(j) for j in i] for i in light_to_temperature_map]

    temperature_to_humidity_raw = split_list[6][1:]
    temperature_to_humidity_map = [i.split(' ') for i in temperature_to_humidity_raw]
    temperature_to_humidity_map = [[int(j) for j in i] for i in temperature_to_humidity_map]

    humidity_to_location_raw = split_list[7][1:]
    humidity_to_location_map = [i.split(' ') for i in humidity_to_location_raw]
    humidity_to_location_map = [[int(j) for j in i] for i in humidity_to_location_map]


    final_location = 100000000000000000000000

    for seed in seeds:
        soil = None
        fertilizer = None
        temperature = None
        water = None
        light = None
        humidity = None
        location = None

        for single_seed_to_soil_map in seed_to_soil_map:
            if seed in range(single_seed_to_soil_map[1], single_seed_to_soil_map[1] + single_seed_to_soil_map[2]):
                soil = seed - single_seed_to_soil_map[1] + single_seed_to_soil_map[0]
                break
        soil = seed if not soil else soil

        for single_soil_to_fertilizer_map in soil_to_fertilizer_map:
            if soil in range(single_soil_to_fertilizer_map[1], single_soil_to_fertilizer_map[1] + single_soil_to_fertilizer_map[2]):
                fertilizer = soil - single_soil_to_fertilizer_map[1] + single_soil_to_fertilizer_map[0]
                break
        fertilizer = soil if not fertilizer else fertilizer

        for single_fertilizer_to_water_map in fertilizer_to_water_map:
            if fertilizer in range(single_fertilizer_to_water_map[1], single_fertilizer_to_water_map[1] + single_fertilizer_to_water_map[2]):
                water = fertilizer - single_fertilizer_to_water_map[1] + single_fertilizer_to_water_map[0]
                break
        water = fertilizer if not water else water

        for single_water_to_light_map in water_to_light_map:
            if water in range(single_water_to_light_map[1], single_water_to_light_map[1] + single_water_to_light_map[2]):
                light = water - single_water_to_light_map[1] + single_water_to_light_map[0]
                break
        light = water if not light else light

        for single_light_to_temperature_map in light_to_temperature_map:
            if light in range(single_light_to_temperature_map[1], single_light_to_temperature_map[1] + single_light_to_temperature_map[2]):
                temperature = light - single_light_to_temperature_map[1] + single_light_to_temperature_map[0]
                break
        temperature = light if not temperature else temperature

        for single_temperature_to_humidity_map in temperature_to_humidity_map:
            if temperature in range(single_temperature_to_humidity_map[1], single_temperature_to_humidity_map[1] + single_temperature_to_humidity_map[2]):
                humidity = temperature - single_temperature_to_humidity_map[1] + single_temperature_to_humidity_map[0]
                break
        humidity = temperature if not humidity else humidity

        for single_humidity_to_location_map in humidity_to_location_map:
            if humidity in range(single_humidity_to_location_map[1], single_humidity_to_location_map[1] + single_humidity_to_location_map[2]):
                location = humidity - single_humidity_to_location_map[1] + single_humidity_to_location_map[0]
                break
        location = humidity if not location else location

        print(f"seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}")

        if location < final_location:
            final_location = location


    print('final_location: ', final_location)


def aoc_day_5a(input_text):
    extract_maps(input_text)


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_5_test_input.txt")
    #print('parsed_file: ', parsed_file)
    aoc_day_5a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_5_actual_input.txt")
    aoc_day_5a(parsed_file)




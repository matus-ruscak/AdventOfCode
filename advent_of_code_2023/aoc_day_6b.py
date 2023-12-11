from utils import parse_text_file_by_line


def aoc_day_6a(input_text):
    time = input_text[0].replace('Time: ', '')
    time = int(time.strip().replace(' ',''))
    print(time)

    distance = input_text[1].replace('Distance: ', '')
    distance = int(distance.strip().replace(' ',''))
    print(distance)

    number_of_winning_combinations = []

    winning_distance = distance
    winning_count = 0
    for j in range(time):
        distance = j * (time - j)
        #print('distance: ', distance)
        if distance > winning_distance:
            winning_count += 1
    number_of_winning_combinations.append(winning_count)

    result = 1
    for i in number_of_winning_combinations:
        result *= i

    print('result: ', result)

    return result


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_6_test_input.txt")
    assert aoc_day_6a(parsed_file) == 71503

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_6_actual_input.txt")
    aoc_day_6a(parsed_file)

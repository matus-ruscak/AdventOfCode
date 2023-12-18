from utils import parse_text_file_by_line
import math


def findsteps(start, instructions, location_dict):
    current_pos = start
    step = 0
    while not current_pos.endswith('Z'):
        current_ins = int(instructions[step % len(instructions)])
        current_pos = location_dict[current_pos][current_ins]
        step += 1
    return step


def aoc_day_8b(input_text):
    instructions_raw = input_text[0]
    instructions = instructions_raw.replace('L', '0').replace('R', '1')
    print('length of instructions: ', len(instructions))

    location_dict = {}

    for step in input_text[2:len(input_text)]:
        current_location = step[0:3]
        left_location = step[7:10]
        right_location = step[12:15]
        location_dict[current_location] = (left_location, right_location)

    print('location_dict: ', location_dict)

    lst = []

    for location in location_dict:
        if location.endswith('A'):
            lst.append(findsteps(location, instructions, location_dict))

    print('lst: ', lst)

    print('result: ', math.lcm(*lst))

    return math.lcm(*lst)


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_8_test_input.txt")
    assert 6 == aoc_day_8b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_8_actual_input.txt")
    aoc_day_8b(parsed_file)

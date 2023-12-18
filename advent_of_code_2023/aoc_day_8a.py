from utils import parse_text_file_by_line


def aoc_day_8a(input_text):
    instructions_raw = input_text[0]
    instructions = instructions_raw.replace('L', '0').replace('R', '1')

    location_dict = {}

    for step in input_text[2:len(input_text)]:
        current_location = step[0:3]
        left_location = step[7:10]
        right_location = step[12:15]
        location_dict[current_location] = (left_location, right_location)

    current_location = 'AAA'
    number_of_steps = 0

    while current_location != 'ZZZ':
        current_instruction = int(instructions[number_of_steps % len(instructions)])
        target_tuple = location_dict[current_location]
        current_location = target_tuple[current_instruction]
        number_of_steps += 1

    print('number_of_steps: ', number_of_steps)

    return number_of_steps


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_8_test_input.txt")
    assert 6 == aoc_day_8a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_8_actual_input.txt")
    aoc_day_8a(parsed_file)

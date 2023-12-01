from utils import parse_text_file_by_line


def aoc_day_1a(input_text):
    result_list_of_digits = []
    for line in input_text:
        line_digits = []
        for character in line:
            if character.isnumeric():
                line_digits.append(character)
        line_number = int(line_digits[0] + line_digits[-1])

        result_list_of_digits.append(line_number)

    total_sum = 0
    for item in result_list_of_digits:
        total_sum += item

    print('resulting sum: ', total_sum)

    return total_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_1_test_input.txt")
    assert aoc_day_1a(parsed_file) == 142

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_1_actual_input.txt")
    aoc_day_1a(parsed_file)

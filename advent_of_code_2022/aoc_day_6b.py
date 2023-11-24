from utils import parse_text_file_by_line


def aoc_day_6b(input_text_file):
    code = input_text_file[0]
    result_position = 0

    for i in range(13, len(code)):
        four_characters_string = code[i-14:i]
        result_set = set()

        for letter in four_characters_string:
            result_set.add(letter)
        if len(result_set) == 14:
            result_position = i
            break

    return result_position

if __name__ == '__main__':

    parsed_test_file = parse_text_file_by_line("../input/aoc_day_6_test_input.txt")
    assert aoc_day_6b(parsed_test_file) == 19

    parsed_test_file = parse_text_file_by_line("../input/aoc_day_6_actual_input.txt")
    print('Result: ', aoc_day_6b(parsed_test_file))











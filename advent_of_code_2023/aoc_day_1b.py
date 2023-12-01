from utils import parse_text_file_by_line


mapping_dictionary = {"one": "1",
                      "two": "2",
                      "three": "3",
                      "four": "4",
                      "five": "5",
                      "six": "6",
                      "seven": "7",
                      "eight": "8",
                      "nine": "9"}


def aoc_day_1b(input_text):
    result_list_of_digits = []
    for line in input_text:
        line_digits = {}
        for word, number in mapping_dictionary.items():
            for i in range(len(line)):
                if word == line[i:i+len(word)]:
                    line_digits[i] = int(number)
                elif line[i].isnumeric():
                    line_digits[i] = int(line[i])

        sorted_line_digits = dict(sorted(line_digits.items()))

        line_list_of_digits = []
        for index, value in sorted_line_digits.items():
            line_list_of_digits.append(value)

        line_number = int(str(line_list_of_digits[0]) + str(line_list_of_digits[-1]))

        result_list_of_digits.append(line_number)

    total_sum = 0
    for item in result_list_of_digits:
        total_sum += item

    print('resulting sum: ', total_sum)

    return total_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_1b_test_input.txt")
    assert aoc_day_1b(parsed_file) == 281

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_1_actual_input.txt")
    aoc_day_1b(parsed_file)

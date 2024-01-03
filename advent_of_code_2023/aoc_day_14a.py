from utils import parse_text_file_by_line


def get_final_upstream_position(current_index, line):
    if current_index == 0:
        return 0
    current_index = current_index - 1
    upstream_character = line[current_index]
    if upstream_character in ('O', '#'):
        return current_index + 1
    else:
        return get_final_upstream_position(current_index, line)


def aoc_day_14a(input_text):
    y_range = len(input_text)
    x_range = len(input_text[0])

    transposed_input_list = []

    for y in range(y_range):
        transposed_line = {}
        for x in range(x_range):
            transposed_line[x] = input_text[x][y]
        transposed_input_list.append(transposed_line)

    sorted_list = []

    for j in range(len(transposed_input_list)):
        line = transposed_input_list[j]
        for i in range(len(line)):
            if line[i] == 'O':
                final_upstream_position = get_final_upstream_position(i, line)
                if final_upstream_position != i:
                    line[i] = '.'
                    line[final_upstream_position] = 'O'
        sorted_list.append(line)

    result_sum = 0

    for line in sorted_list:
        line_length = len(line)
        for j in range(line_length):
            if line[j] == 'O':
                result_sum += (line_length - j)

    print('result_sum: ', result_sum)

    return result_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_14_test_input.txt")
    assert 136 == aoc_day_14a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_14_actual_input.txt")
    aoc_day_14a(parsed_file)
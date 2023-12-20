from utils import parse_text_file_by_line


def calculate_diffs(sequence, current_sum):
    if set(sequence) != {0}:
        diff_list = []
        for i in range(len(sequence) - 1):
            diff_list.append(sequence[i + 1] - sequence[i])
        current_sum += diff_list[-1]
        return calculate_diffs(diff_list, current_sum)
    else:
        return current_sum


def aoc_day_9a(input_text):
    result_sum = 0

    for line in input_text:
        sequence = line.split(' ')
        int_sequence = [int(i) for i in sequence]

        to_be_added = calculate_diffs(int_sequence, 0)
        item_number = int_sequence[-1] + to_be_added
        result_sum += item_number

    print('RESULT SUM: ', result_sum)

    return result_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_9_test_input.txt")
    assert 114 == aoc_day_9a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_9_actual_input.txt")
    aoc_day_9a(parsed_file)

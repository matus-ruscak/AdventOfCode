from utils import parse_text_file_by_line


def calculate_diffs(sequence, current_factor_list):
    if set(sequence) != {0}:
        diff_list = []
        for i in range(len(sequence) - 1):
            diff_list.append(sequence[i] - sequence[i+1])
        current_factor_list.append(diff_list[-1])
        return calculate_diffs(diff_list, current_factor_list)
    else:
        return current_factor_list


def aoc_day_9b(input_text):
    result_sum = 0

    for line in input_text:
        sequence = line.split(' ')
        int_sequence = [int(i) for i in sequence]
        int_sequence.reverse()
        to_be_added = calculate_diffs(int_sequence, [int_sequence[-1]])
        result_number = to_be_added[0]
        calc_numbers = to_be_added[1:]
        for i in range(len(calc_numbers)):
            if (i % 2) == 0:
                result_number -= calc_numbers[i]
            else:
                result_number += calc_numbers[i]

        result_sum += result_number

    print('result_sum: ', result_sum)

    return result_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_9_test_input.txt")
    assert 2 == aoc_day_9b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_9_actual_input.txt")
    aoc_day_9b(parsed_file)

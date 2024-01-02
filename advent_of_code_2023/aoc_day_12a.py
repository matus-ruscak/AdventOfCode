from utils import parse_text_file_by_line
import re
import itertools


def aoc_day_12a(input_text):
    final_number_of_combinations = 0
    for line_index in range(len(input_text)):
        line = input_text[line_index]
        pipe_states = line.split(' ')[0]
        group_labels = line.split(' ')[1]
        group_labels = group_labels.split(',')
        group_labels = [int(i) for i in group_labels]
        indices_of_wildcard = [m.start() for m in re.finditer('\?', pipe_states)]
        num_of_wildcards = len(indices_of_wildcard)

        num_of_valid_combinations = 0

        for i in range(num_of_wildcards+1):
            combinations = list(itertools.combinations(indices_of_wildcard, i))
            for j in range(len(combinations)):
                indices_to_be_replaced = combinations[j]
                indices_split = sorted(list(indices_to_be_replaced))
                result_string = ''
                for k in range(len(pipe_states)):
                    if pipe_states[k] == '?':
                        if k in indices_split:
                            result_string = result_string + '#'
                        else:
                            result_string = result_string + '.'
                    else:
                        result_string = result_string + pipe_states[k]
                result_groups = result_string.split('.')
                result_groups = [i for i in result_groups if i != '']
                result_lengths = [len(i) for i in result_groups]
                if result_lengths == group_labels:
                    num_of_valid_combinations += 1

        final_number_of_combinations += num_of_valid_combinations
        print('line: ', line, ' added ', num_of_valid_combinations, 'combinations')
    print('FINAL number of combinations: ', final_number_of_combinations)

    return final_number_of_combinations


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_12_test_input.txt")
    assert 21 == aoc_day_12a(parsed_file)

    # parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_12_actual_input.txt")
    # aoc_day_12a(parsed_file)
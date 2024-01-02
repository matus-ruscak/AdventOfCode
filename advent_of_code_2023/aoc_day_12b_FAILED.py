from utils import parse_text_file_by_line
import re
import itertools


def unfold_the_lines(pipe_states, group_labels):
    result_pipe_states = pipe_states + '?' + pipe_states

    result_group_labels = group_labels * 2

    return result_pipe_states, result_group_labels


def calculate_num_of_combinations(num_of_wildcards, indices_of_wildcard, pipe_states, group_labels):
    num_of_valid_combinations = 0
    for i in range(num_of_wildcards + 1):
        combinations = list(itertools.combinations(indices_of_wildcard, i))
        #print('len(combinations): ', len(combinations))
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
            #print('result_string: ', result_string)
            result_groups = result_string.split('.')
            result_groups = [i for i in result_groups if i != '']
            result_lengths = [len(i) for i in result_groups]
            if result_lengths == group_labels:
                num_of_valid_combinations += 1

    return num_of_valid_combinations


def aoc_day_12b(input_text):
    final_number_of_combinations = 0
    for line_index in range(len(input_text)):
        print('line_index: ', line_index)
        line = input_text[line_index]
        print('line: ', line)
        pipe_states = line.split(' ')[0]
        group_labels = line.split(' ')[1]
        group_labels = group_labels.split(',')
        group_labels = [int(i) for i in group_labels]
        indices_of_wildcard = [m.start() for m in re.finditer('\?', pipe_states)]
        num_of_wildcards = len(indices_of_wildcard)
        print('num_of_wildcards: ', num_of_wildcards)
        initial_number_of_combinations = calculate_num_of_combinations(num_of_wildcards,
                                                                       indices_of_wildcard,
                                                                       pipe_states,
                                                                       group_labels)
        print('initial_number_of_combinations: ', initial_number_of_combinations)

        doubled_pipe_states, doubled_group_labels = unfold_the_lines(pipe_states, group_labels)
        doubled_indices_of_wildcard = [m.start() for m in re.finditer('\?', doubled_pipe_states)]
        num_of_doubled_wildcards = len(doubled_indices_of_wildcard)

        doubled_number_of_combinations = calculate_num_of_combinations(num_of_doubled_wildcards,
                                                                       doubled_indices_of_wildcard,
                                                                       doubled_pipe_states,
                                                                       doubled_group_labels)
        print('doubled_number_of_combinations: ', doubled_number_of_combinations)

        result_number_of_valid_combinations = ((round(doubled_number_of_combinations / initial_number_of_combinations)) ** 4) *  initial_number_of_combinations

        final_number_of_combinations += result_number_of_valid_combinations
        print('num_of_valid_combinations: ', result_number_of_valid_combinations)
        print('')

    print('FINAL number of combinations: ', final_number_of_combinations)

    return final_number_of_combinations


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_12_test_input.txt")
    assert 525152 == aoc_day_12b(parsed_file) # Started at 20:07

    # parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_12_actual_input.txt")
    # aoc_day_12b(parsed_file) # Started at 10:48
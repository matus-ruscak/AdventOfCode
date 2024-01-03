from utils import parse_text_file_by_line


def get_final_upstream_position(current_index, line):
    if current_index == (len(line) - 1):
        return len(line) - 1
    current_index = current_index + 1
    upstream_character = line[current_index]
    if upstream_character in ('O', '#'):
        return current_index - 1
    else:
        return get_final_upstream_position(current_index, line)


def transpose_input_list(y_range, x_range, input_text):
    result_transposed_list = []

    for y in range(y_range):
        transposed_line = {}
        for x in range(x_range):
            transposed_line[x] = input_text[(x_range-1)-x][y]
        result_transposed_list.append(transposed_line)

    return result_transposed_list


def transpose_dict_90_degrees(input_dict_list):
    y_range = len(input_dict_list)
    x_range = len(input_dict_list[0])

    transposed_dict_list = []

    for y in range(y_range):
        transposed_dict = {}
        for x in range(x_range):
            transposed_dict[x] = input_dict_list[(x_range-1) - x][y]
        transposed_dict_list.append(transposed_dict)

    return transposed_dict_list
    

def move_rocks(input_list_dict):
    sorted_list = []

    for j in range(len(input_list_dict)):
        line = input_list_dict[j]
        for i in reversed(range(len(line))):
            if line[i] == 'O':
                final_upstream_position = get_final_upstream_position(i, line)
                if final_upstream_position != i:
                    line[i] = '.'
                    line[final_upstream_position] = 'O'
        sorted_list.append(line)

    return sorted_list


def calculate_result_sum(sorted_list):
    result_sum = 0

    for line in sorted_list:
        line_length = len(line)
        for j in range(line_length):
            if line[j] == 'O':
                result_sum += j + 1

    return result_sum


def process_cycles(input_list, number_of_cycles):
    original_number_of_cycles = number_of_cycles
    number_of_cycles = number_of_cycles * 4

    result_sum_dict = {}

    while number_of_cycles > 0:
        moved_rocks = move_rocks(input_list)
        transposed_rocks = transpose_dict_90_degrees(moved_rocks)

        number_of_cycles = number_of_cycles - 1
        input_list = transposed_rocks

        if number_of_cycles % 4 == 0:
            current_cycle = original_number_of_cycles - round(number_of_cycles/4)
            current_sum = calculate_result_sum(input_list)
            if current_sum in result_sum_dict.values():
                duplicate_count = 0
                for cycle, value in result_sum_dict.items():
                    if current_sum == value:
                        duplicate_count += 1
                if duplicate_count > 6:
                    return result_sum_dict, input_list
                else:
                    result_sum_dict[current_cycle] = current_sum
            else:
                result_sum_dict[current_cycle] = current_sum

    return result_sum_dict, input_list


def aoc_day_14a(input_text):
    y_range = len(input_text)
    x_range = len(input_text[0])

    # Transpose the list
    transposed_input_list = transpose_input_list(y_range, x_range, input_text)
    sorted_list = transposed_input_list

    result_sum_dict, result_list = process_cycles(sorted_list, 400)

    max_cycle = 0
    max_sum = 0
    for cycle, result_sum in result_sum_dict.items():
        if cycle > max_cycle:
            max_cycle = cycle
            max_sum = result_sum

    next_closest_cycle = 0
    for cycle, result_sum in result_sum_dict.items():
        if (result_sum == max_sum) and (cycle != max_cycle) and (cycle > next_closest_cycle):
            next_closest_cycle = cycle

    full_number_of_cycles = 1000000000
    reduced_number_of_cycles = full_number_of_cycles - next_closest_cycle
    cycle_shift_to_get_the_result = reduced_number_of_cycles % (max_cycle - next_closest_cycle)
    dict_index_of_the_result = next_closest_cycle + cycle_shift_to_get_the_result

    final_result = result_sum_dict[dict_index_of_the_result]

    print('final_result: ', final_result)

    return final_result


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_14_test_input.txt")
    assert 64 == aoc_day_14a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_14_actual_input.txt")
    aoc_day_14a(parsed_file)
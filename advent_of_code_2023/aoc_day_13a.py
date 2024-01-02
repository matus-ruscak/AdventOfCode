from utils import parse_text_file_by_line, return_split_list


def generate_comparison_ranges(x_range, y_range):
    vertical_combinations = []
    for outer_x in range(1, x_range):
        single_vertical_combination = [[outer_x, outer_x - 1], ]
        min_distance_to_edge = min(outer_x, x_range - outer_x)
        for inner_x in range(1, min_distance_to_edge):
            single_vertical_combination.append([outer_x - inner_x - 1, outer_x + inner_x])
        vertical_combinations.append(single_vertical_combination)

    horizontal_combinations = []
    for outer_y in range(1, y_range):
        single_horizontal_combination = [[outer_y, outer_y - 1], ]
        min_distance_to_edge = min(outer_y, y_range - outer_y)
        for inner_y in range(1, min_distance_to_edge):
            single_horizontal_combination.append([outer_y - inner_y - 1, outer_y + inner_y])
        horizontal_combinations.append(single_horizontal_combination)

    return vertical_combinations, horizontal_combinations


def aoc_day_13a(input_text):
    patterns = return_split_list(input_text, '')
    result_sum = 0

    for pattern in patterns:
        x_range = len(pattern[0])
        y_range = len(pattern)

        vertical_combinations, horizontal_combinations = generate_comparison_ranges(x_range, y_range)

        # Check vertical lines
        for i in range(len(vertical_combinations)):
            matching_vertical_line = True
            for vertical_combination in vertical_combinations[i]:
                for y in range(y_range):
                    if pattern[y][vertical_combination[0]] != pattern[y][vertical_combination[1]]:
                        matching_vertical_line = False
            if matching_vertical_line:
                result_sum += i + 1

        # Check horizontal lines
        for i in range(len(horizontal_combinations)):
            matching_horizontal_line = True
            for horizontal_combination in horizontal_combinations[i]:
                for x in range(x_range):
                    if pattern[horizontal_combination[0]][x] != pattern[horizontal_combination[1]][x]:
                        matching_horizontal_line = False
            if matching_horizontal_line:
                result_sum += (i + 1) * 100

    print('RESULT_SUM: ', result_sum)

    return result_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_13_test_input.txt")
    assert 405 == aoc_day_13a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_13_actual_input.txt")
    aoc_day_13a(parsed_file)
    # correct 32723
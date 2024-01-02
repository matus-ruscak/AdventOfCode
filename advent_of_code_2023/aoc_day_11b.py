from utils import parse_text_file_by_line


def aoc_day_11b(input_text):
    print(input_text)
    y_range = len(input_text)
    x_range = len(input_text[0])

    star_locations = []
    for i in range(0, y_range):
        for j in range(0, x_range):
            if input_text[i][j] == "#":
                star_locations.append((i, j))

    # check empty rows
    empty_rows = []
    for i in range(0, y_range):
        if set(input_text[i]) == {'.'}:
            empty_rows.append(i)

    # check empty columns
    empty_columns = []
    for j in range(0, x_range):
        check_column = set()
        for i in range(0, y_range):
            check_column.add(input_text[i][j])
        if check_column == {'.'}:
            empty_columns.append(j)

    # calculate distances
    checked_pairs = []
    final_distance = 0
    for i in star_locations:
        for j in star_locations:
            if (i != j) and ((i, j) not in checked_pairs) and ((j, i) not in checked_pairs):
                y_distance = abs(i[0] - j[0])
                x_distance = abs(i[1] - j[1])
                distance = x_distance + y_distance
                for empty_row in empty_rows:
                    if empty_row in range(min(i[0], j[0]), max(i[0], j[0]) + 1):
                        distance += (1000000 - 1)
                for empty_col in empty_columns:
                    if empty_col in range(min(i[1], j[1]), max(i[1], j[1]) + 1):
                        distance += (1000000 - 1)
                checked_pairs.append((i, j))
                final_distance += distance
    print('FINAL DISTANCE: ', final_distance)
    return final_distance


if __name__ == '__main__':
    # parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_11_test_input.txt")
    # assert 1030 == aoc_day_11b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_11_actual_input.txt")
    aoc_day_11b(parsed_file)

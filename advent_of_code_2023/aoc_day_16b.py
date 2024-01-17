from utils import parse_text_file_by_line


def navigate_and_count_tiles(current_position, previous_shift, input_text, all_tiles):
    current_y = current_position[0]
    current_x = current_position[1]
    current_character = input_text[current_y][current_x]

    new_shifts = []

    if current_character == '.':
        new_shifts = [previous_shift]
    elif current_character == '/':
        if previous_shift == (0, 1):
            new_shifts = [(-1, 0)]
        elif previous_shift == (0, -1):
            new_shifts = [(1, 0)]
        elif previous_shift == (1, 0):
            new_shifts = [(0, -1)]
        elif previous_shift == (-1, 0):
            new_shifts = [(0, 1)]
    elif current_character == '\\':
        if previous_shift == (0, 1):
            new_shifts = [(1, 0)]
        elif previous_shift == (0, -1):
            new_shifts = [(-1, 0)]
        elif previous_shift == (1, 0):
            new_shifts = [(0, 1)]
        elif previous_shift == (-1, 0):
            new_shifts = [(0, -1)]
    elif current_character == '|':
        if previous_shift in [(1, 0), (-1, 0)]:
            new_shifts = [previous_shift]
        elif previous_shift in [(0, 1), (0, -1)]:
            new_shifts = [(-1, 0), (1, 0)]
    elif current_character == '-':
        if previous_shift in [(0, 1), (0, -1)]:
            new_shifts = [previous_shift]
        elif previous_shift in [(1, 0), (-1, 0)]:
            new_shifts = [(0, -1), (0, 1)]

    new_returned_positions = []
    new_returned_shifts = []
    for shift in new_shifts:
        # check if it's not out of range
        new_y = current_position[0] + shift[0]
        new_x = current_position[1] + shift[1]
        if (new_y in range(len(input_text))) and (new_x in range(len(input_text[0]))):
            new_position = (new_y, new_x)
            all_tiles.add(new_position)
            new_returned_positions.append(new_position)
            new_returned_shifts.append(shift)
    return new_returned_positions, new_returned_shifts, input_text, all_tiles


def aoc_day_16b(input_text):
    energized_tiles = set()

    y_range = len(input_text)
    x_range = len(input_text[0])

    starting_positions = []
    starting_shifts = []

    for x in range(x_range):
        starting_positions.append((0, x))
        starting_shifts.append((1, 0))

    for x in range(x_range):
        starting_positions.append((y_range-1, x))
        starting_shifts.append((-1, 0))

    for y in range(y_range):
        starting_positions.append((y, 0))
        starting_shifts.append((0, 1))

    for y in range(y_range):
        starting_positions.append((y, x_range - 1))
        starting_shifts.append((0, -1))

    # print('starting_positions: ', starting_positions)
    # print('starting_shifts: ', starting_shifts)
    # print('length of starting_positions: ', len(starting_positions))
    # print('length of starting_shifts: ', len(starting_shifts))

    for i in range(len(starting_positions)):
        # print('i: ', i)
        current_positions = [starting_positions[i]]
        previous_shifts = [starting_shifts[i]]
        all_tiles = {starting_positions[i]}

        counter = 0
        while True:
            counter += 1
            # Optimization - after a while, the loops get multiplying at each junction - this is to limit the number of
            # maximum length of current_positions
            cleaned_set = set()
            for i in range(len(current_positions)):
                cleaned_set.add((current_positions[i], previous_shifts[i]))
            current_positions = []
            previous_shifts = []
            for j in cleaned_set:
                current_positions.append(j[0])
                previous_shifts.append(j[1])

            if len(current_positions) == 0:
                #print('Finished with the set: ', all_tiles)
                print('Number of visited tiles: ', len(all_tiles))
                break
            if counter > 1500:
                #print('Finished with the set: ', all_tiles)
                print('Number of visited tiles: ', len(all_tiles))
                break
            next_positions = []
            next_previous_shifts = []
            for i in range(len(current_positions)):
                current_position = current_positions[i]
                previous_shift = previous_shifts[i]
                try:
                    new_positions, new_previous_shifts, input_text, all_tiles = navigate_and_count_tiles(current_position,
                                                                                                         previous_shift,
                                                                                                         input_text,
                                                                                                         all_tiles)
                    next_positions.extend(new_positions)
                    next_previous_shifts.extend(new_previous_shifts)
                except IndexError:
                    print('Caught IndexError')

            current_positions = next_positions
            previous_shifts = next_previous_shifts

        energized_tiles.add(len(all_tiles))

    print('PRINTING MAX RESULT: ', max(energized_tiles))
    return max(energized_tiles)


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_16_test_input.txt")
    assert 51 == aoc_day_16b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_16_actual_input.txt")
    aoc_day_16b(parsed_file)

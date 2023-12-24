from utils import parse_text_file_by_line


def decode_instruction(character, shift):
    instruction = None

    match character:
        case "|":
            if shift[0] == 1:
                instruction = (1, 0)
            elif shift[0] == -1:
                instruction = (-1, 0)
        case "-":
            if shift[1] == 1:
                instruction = (0, 1)
            elif shift[1] == -1:
                instruction = (0, -1)
        case "L":
            if shift == (1, 0):
                instruction = (0, 1)
            elif shift == (0, -1):
                instruction = (-1, 0)
        case "J":
            if shift == (0, 1):
                instruction = (-1, 0)
            elif shift == (1, 0):
                instruction = (0, -1)
        case "7":
            if shift == (-1, 0):
                instruction = (0, -1)
            elif shift == (0, 1):
                instruction = (1, 0)
        case "F":
            if shift == (0, -1):
                instruction = (1, 0)
            elif shift == (-1, 0):
                instruction = (0, 1)
        case ".":
            instruction = None
        case _:
            instruction = None

    return instruction


def navigate_map(full_map, current_position, character, shift, step_count):
    shift = decode_instruction(character, shift)
    if shift:
        current_position = (current_position[0] + shift[0], current_position[1] + shift[1])
        character = full_map[current_position[0]][current_position[1]]
        if character == 'S':
            step_count += 1
            return current_position, character, shift, step_count
        else:
            step_count += 1
            return current_position, character, shift, step_count
    else:
        print('DEAD END')
        return current_position, character, shift, step_count


def aoc_day_10b(input_text):
    full_map = []
    for line in input_text:
        full_map.append([i for i in line])

    start_position = (0, 0)

    for i in range(len(full_map)):
        for j in range(len(full_map[i])):
            if "S" == full_map[i][j]:
                start_position = (i, j)

    print('start_position: ', start_position)
    possible_shifts = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    y_range = len(full_map)
    x_range = len(full_map[0])

    for possible_shift in possible_shifts:
        step_count = 1
        current_position = (start_position[0] + possible_shift[0], start_position[1] + possible_shift[1])
        all_positions = []
        all_positions.append(current_position)
        character = full_map[current_position[0]][current_position[1]]
        shift = possible_shift
        while True:
            current_position, character, shift, step_count = navigate_map(full_map, current_position, character, shift, step_count)
            all_positions.append(current_position)
            if character == 'S':
                print('FOUND S after: ', step_count, ' steps')
                print('STEP COUNT DIVIDED BY 2: ', round(step_count / 2))
                return round(step_count / 2), all_positions, y_range, x_range, full_map
            if shift is None:
                break


if __name__ == '__main__':
    # parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_10_test_input_b_2.txt")
    # tep_count, all_positions, y_range, x_range, full_map = aoc_day_10b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_10_actual_input.txt")
    step_count, all_positions, y_range, x_range, full_map = aoc_day_10b(parsed_file)
    # 32 is wrong, 37 is wrong

    # Calculate the number of points
    # points go from [0,0] until [8, 10]
    possible_positions = []
    for i in range(y_range):
        for j in range(x_range):
            if (i, j) not in all_positions:
                possible_positions.append((i, j))

    final_positions = set()

    # Empty positions - potential candidates
    for possible_position in possible_positions:
        left_border = (0, 0)
        right_border = (0, 0)
        top_border = (0, 0)
        bottom_border = (0, 0)

        # Check each position and see if the wall is "complete" - if it has both sides
        for i in range(len(all_positions)):
            step_position = all_positions[i]

            # Horizontal borders
            if step_position[0] == possible_position[0]:
                # Left borders
                if step_position[1] < possible_position[1]:
                    if i > 0:
                        if all_positions[i - 1][0] > step_position[0]:
                            left_border = (left_border[0] + 1, left_border[1])
                        elif all_positions[i - 1][0] < step_position[0]:
                            left_border = (left_border[0], left_border[1] + 1)
                    else:
                        if all_positions[-1][0] > step_position[0]:
                            left_border = (left_border[0] + 1, left_border[1])
                        elif all_positions[-1][0] < step_position[0]:
                            left_border = (left_border[0], left_border[1] + 1)

                    if i < len(all_positions) - 1:
                        if all_positions[i + 1][0] > step_position[0]:
                            left_border = (left_border[0] + 1, left_border[1])
                        elif all_positions[i + 1][0] < step_position[0]:
                            left_border = (left_border[0], left_border[1] + 1)
                    else:
                        if all_positions[0][0] > step_position[0]:
                            left_border = (left_border[0] + 1, left_border[1])
                        elif all_positions[0][0] < step_position[0]:
                            left_border = (left_border[0], left_border[1] + 1)

                # Right borders
                if step_position[1] > possible_position[1]:
                    if i > 0:
                        if all_positions[i - 1][0] > step_position[0]:
                            right_border = (right_border[0] + 1, right_border[1])
                        elif all_positions[i - 1][0] < step_position[0]:
                            right_border = (right_border[0], right_border[1] + 1)
                    else:
                        if all_positions[-1][0] > step_position[0]:
                            right_border = (right_border[0] + 1, right_border[1])
                        elif all_positions[-1][0] < step_position[0]:
                            right_border = (right_border[0], right_border[1] + 1)

                    if i < len(all_positions) - 1:
                        if all_positions[i + 1][0] > step_position[0]:
                            right_border = (right_border[0] + 1, right_border[1])
                        elif all_positions[i + 1][0] < step_position[0]:
                            right_border = (right_border[0], right_border[1] + 1)
                    else:
                        if all_positions[0][0] > step_position[0]:
                            right_border = (right_border[0] + 1, right_border[1])
                        elif all_positions[0][0] < step_position[0]:
                            right_border = (right_border[0], right_border[1] + 1)

            # Vertical borders
            if step_position[1] == possible_position[1]:
                # Top Borders
                if step_position[0] < possible_position[0]:
                    if i > 0:
                        if all_positions[i - 1][1] > step_position[1]:
                            top_border = (top_border[0] + 1, top_border[1])
                        elif all_positions[i - 1][1] < step_position[1]:
                            top_border = (top_border[0], top_border[1] + 1)
                    else:
                        if all_positions[-1][1] > step_position[1]:
                            top_border = (top_border[0] + 1, top_border[1])
                        elif all_positions[-1][1] < step_position[1]:
                            top_border = (top_border[0], top_border[1] + 1)

                    if i < len(all_positions) - 1:
                        if all_positions[i + 1][1] > step_position[1]:
                            top_border = (top_border[0] + 1, top_border[1])
                        elif all_positions[i + 1][1] < step_position[1]:
                            top_border = (top_border[0], top_border[1] + 1)
                    else:
                        if all_positions[0][1] > step_position[1]:
                            top_border = (top_border[0] + 1, top_border[1])
                        elif all_positions[0][1] < step_position[1]:
                            top_border = (top_border[0], top_border[1] + 1)

                # Bottom Borders
                if step_position[0] > possible_position[0]:
                    if i > 0:
                        if all_positions[i - 1][1] > step_position[1]:
                            bottom_border = (bottom_border[0] + 1, bottom_border[1])
                        elif all_positions[i - 1][1] < step_position[1]:
                            bottom_border = (bottom_border[0], bottom_border[1] + 1)
                    else:
                        if all_positions[-1][1] > step_position[1]:
                            bottom_border = (bottom_border[0] + 1, bottom_border[1])
                        elif all_positions[-1][1] < step_position[1]:
                            bottom_border = (bottom_border[0], bottom_border[1] + 1)

                    if i < len(all_positions) - 1:
                        if all_positions[i + 1][1] > step_position[1]:
                            bottom_border = (bottom_border[0] + 1, bottom_border[1])
                        elif all_positions[i + 1][1] < step_position[1]:
                            bottom_border = (bottom_border[0], bottom_border[1] + 1)
                    else:
                        if all_positions[0][1] > step_position[1]:
                            bottom_border = (bottom_border[0] + 1, bottom_border[1])
                        elif all_positions[0][1] < step_position[1]:
                            bottom_border = (bottom_border[0], bottom_border[1] + 1)

        left_border = left_border[0] if left_border[0] < left_border[1] else left_border[1]
        right_border = right_border[0] if right_border[0] < right_border[1] else right_border[1]
        top_border = top_border[0] if top_border[0] < top_border[1] else top_border[1]
        bottom_border = bottom_border[0] if bottom_border[0] < bottom_border[1] else bottom_border[1]

        if (left_border % 2 == 1) and (right_border % 2 == 1) and (top_border % 2 == 1) and (bottom_border % 2 == 1) and left_border > 0 and right_border > 0 and top_border > 0 and bottom_border > 0:
            final_positions.add(possible_position)

    print('FINAL NUMBER OF TILES INSIDE: ', len(final_positions))

    # Plot the output
    import matplotlib.pyplot as plt
    import numpy as np

    plt.scatter(*zip(*all_positions))
    plt.plot(*zip(*all_positions))
    plt.xlim([-1, y_range])
    plt.xticks(np.arange(0, y_range, 1.0))
    plt.ylim([-1, x_range])
    plt.yticks(np.arange(0, x_range, 1.0))
    plt.plot(*zip(*all_positions))
    plt.scatter(*zip(*final_positions))
    plt.show()



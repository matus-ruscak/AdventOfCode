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


def aoc_day_10a(input_text):
    full_map = []
    for line in input_text:
        full_map.append([i for i in line])

    start_position = (0, 0)

    for i in range(len(full_map)):
        for j in range(len(full_map[i])):
            if "S" == full_map[i][j]:
                start_position = (i, j)

    possible_shifts = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for possible_shift in possible_shifts:
        step_count = 1
        current_position = (start_position[0] + possible_shift[0], start_position[1] + possible_shift[1])
        character = full_map[current_position[0]][current_position[1]]
        shift = possible_shift
        while True:
            current_position, character, shift, step_count = navigate_map(full_map, current_position, character, shift, step_count)
            if character == 'S':
                print('FOUND S after: ', step_count, ' steps')
                print('STEP COUNT DIVIDED BY 2: ', round(step_count / 2))
                return round(step_count / 2)
            if shift is None:
                break
        print('')


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_10_test_input_2.txt")
    assert 4 == aoc_day_10a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_10_test_input.txt")
    assert 8 == aoc_day_10a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_10_actual_input.txt")
    assert 7086 == aoc_day_10a(parsed_file)

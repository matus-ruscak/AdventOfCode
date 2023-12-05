from utils import parse_text_file_by_line


def extract_numbers(input_line):
    numbers_in_line = {}
    j = 0
    while j < len(input_line):
        if input_line[j].isnumeric():
            if j+1 < len(input_line):
                if input_line[j + 1].isnumeric():
                    if j+2 < len(input_line):
                        if input_line[j + 2].isnumeric():
                            numbers_in_line[j] = input_line[j:j + 3]
                            j += 3
                        else:
                            numbers_in_line[j] = input_line[j:j + 2]
                            j += 2
                    else:
                        numbers_in_line[j] = input_line[j:j+1]
                        j += 1
                else:
                    numbers_in_line[j] = input_line[j]
                    j += 1
            else:
                numbers_in_line[j] = input_line[j]
                j += 1
        else:
            j += 1

    return numbers_in_line


def extract_stars(input_line):
    stars_in_line = []
    j = 0
    while j < len(input_line):
        if input_line[j] == '*':
            stars_in_line.append(j)
        j += 1

    return stars_in_line


def aoc_day_3b(input_text):
    result_gears = []

    for i in range(len(input_text)):
        current_line = input_text[i]
        numbers_in_line = extract_numbers(current_line)
        stars_in_line = extract_stars(current_line)

        # Case 1 - star on the same line
        for index, number in numbers_in_line.items():
            for star in stars_in_line:
                for rev_index, rev_number in numbers_in_line.items():
                    if index != rev_index:
                        if (star == index + len(number)) and (star == rev_index - 1):
                            result_gears.append(int(number) * int(rev_number))
                            print(f'line {i+1}, case 1, multiplying {number} * {rev_number} to get '
                                  f'{int(number) * int(rev_number)}')

        # Case 2 - star on the SAME line and number on the NEXT one
        if i < len(input_text) - 1:
            next_line = input_text[i+1]
            for index, number in numbers_in_line.items():
                for star in stars_in_line:
                    if (star == index + len(number)) or (star == index - 1):
                        numbers_in_next_line = extract_numbers(next_line)
                        for next_line_index, next_line_num in numbers_in_next_line.items():
                            relevant_star_indices = set(range(star - 1, star + 1 + 1))
                            valid_next_line_number_indices = set(range(next_line_index, next_line_index
                                                                       + len(next_line_num)))
                            if relevant_star_indices.intersection(valid_next_line_number_indices):
                                result_gears.append(int(number) * int(next_line_num))
                                print(f'line {i+1}, case 2, multiplying {number} * {next_line_num} to get '
                                      f'{int(number) * int(next_line_num)}')

        # Case 3 - star and number on the NEXT line and number on the PREVIOUS
            next_line = input_text[i + 1]
            next_line_numbers = extract_numbers(next_line)
            next_line_stars = extract_stars(next_line)
            for next_line_index, next_line_number in next_line_numbers.items():
                for star in next_line_stars:
                    if (star == next_line_index + len(next_line_number)) or (star == next_line_index - 1):
                        for index, number in numbers_in_line.items():
                            relevant_star_indices = set(range(star - 1, star + 1 + 1))
                            valid_line_number_indices = set(
                                range(index, index + len(number)))
                            if relevant_star_indices.intersection(valid_line_number_indices):
                                result_gears.append(int(number) * int(next_line_number))
                                print(f'line {i+1}, case 3, multiplying {number} * {next_line_number} to get '
                                      f'{int(number) * int(next_line_number)}')

        # Case 4 - ONLY star is on the next line
            next_line = input_text[i + 1]
            next_line_stars = extract_stars(next_line)
            for star in next_line_stars:
                for index, number in numbers_in_line.items():
                    if star == index + len(number):
                        for mult_index, mult_number in numbers_in_line.items():
                            if (index != mult_index) and (star == mult_index - 1):
                                result_gears.append(int(number) * int(mult_number))
                                print(f'line {i+1}, case 4, multiplying {number} * {mult_number} to get '
                                      f'{int(number) * int(mult_number)}')

        # Case 5 - ONLY star is on the PREVIOUS line
        if i > 0:
            previous_line = input_text[i - 1]
            previous_line_stars = extract_stars(previous_line)
            for star in previous_line_stars:
                for index, number in numbers_in_line.items():
                    if star == index + len(number):
                        for mult_index, mult_number in numbers_in_line.items():
                            if (index != mult_index) and (star == mult_index - 1):
                                result_gears.append(int(number) * int(mult_number))
                                print(
                                    f'line {i + 1}, case 5, multiplying {number} * {mult_number} to get '
                                    f'{int(number) * int(mult_number)}')

        # Case 5 - star connecting 3 lines
        if i < len(input_text) - 2:
            next_line = input_text[i + 1]
            stars_in_next_line = extract_stars(next_line)
            for index, number in numbers_in_line.items():
                for star in stars_in_next_line:
                    relevant_star_indices = set(range(star - 1, star + 1 + 1))
                    valid_current_line_number_indices = set(range(index, index + len(number)))
                    if relevant_star_indices.intersection(valid_current_line_number_indices):
                        third_line = input_text[i + 2]
                        numbers_in_third_line = extract_numbers(third_line)
                        for third_line_index, number_in_third_line in numbers_in_third_line.items():
                            valid_third_line_number_indices = set(range(third_line_index, third_line_index
                                                                        + len(number_in_third_line)))
                            if relevant_star_indices.intersection(valid_third_line_number_indices):
                                result_gears.append(int(number) * int(number_in_third_line))
                                print(f'line {i+1}, case 5, multiplying {number} * {number_in_third_line} to get '
                                      f'{int(number) * int(number_in_third_line)}')

        print('')

    total_sum = 0
    for i in result_gears:
        total_sum += i

    print('total_sum: ', total_sum)
    print('result_gears: ', result_gears)

    return total_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_3_test_input.txt")
    assert 467835 == aoc_day_3b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_3_actual_input.txt")
    aoc_day_3b(parsed_file)

    # 65565813 too LOW
    # 72493832 too LOW
    # 88186768 too HIGH
    # 84202892 WRONG
    # 85794113 WRONG
    # 84994283 WRONG
    # 83939299 WRONG
    # 79513049 WRONG
    # 83281509 WRONG
    # 385X296 is missing
    # WINNER -> 84584891

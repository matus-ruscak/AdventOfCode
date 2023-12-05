from utils import parse_text_file_by_line


def extract_numbers(input_line):
    number_card = input_line.split(':')[1]
    winning_numbers = number_card.split('|')[0]
    winning_numbers_list = winning_numbers.split(' ')
    winning_numbers_filtered = []
    for i in winning_numbers_list:
        if i.isnumeric():
            winning_numbers_filtered.append(int(i))

    my_numbers = number_card.split('|')[1]
    my_numbers_list = my_numbers.split(' ')
    my_numbers_filtered = []
    for i in my_numbers_list:
        if i.isnumeric():
            my_numbers_filtered.append(int(i))

    return winning_numbers_filtered, my_numbers_filtered


def aoc_day_4a(input_text):
    total_points = 0

    for i in range(len(input_text)):
        line = input_text[i]
        winning_numbers, my_numbers = extract_numbers(line)

        round_points = 0
        for winning_number in winning_numbers:
            for my_number in my_numbers:
                if winning_number == my_number:
                    if round_points == 0:
                        round_points = 1
                    else:
                        round_points *= 2
        total_points += round_points

    print('total_points: ', total_points)

    return total_points


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_4_test_input.txt")
    assert 13 == aoc_day_4a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_4_actual_input.txt")
    aoc_day_4a(parsed_file)



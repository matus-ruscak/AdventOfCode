from utils import parse_text_file_by_line
import re
import copy


def extract_numbers(input_line):
    card_id = int(re.search('Card (.*):', input_line).group(1).strip())
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

    return [card_id, winning_numbers_filtered, my_numbers_filtered]


def aoc_day_4b(input_text):
    original_input_text = copy.deepcopy(input_text)
    total_card_number = len(input_text)

    while len(input_text) > 0:
        line = input_text[0]
        parsed_line = extract_numbers(line)
        card_id = parsed_line[0] - 1  # decrement to match the 0 based numbering of input_text
        winning_numbers = parsed_line[1]
        my_numbers = parsed_line[2]

        round_points = 0
        for winning_number in winning_numbers:
            for my_number in my_numbers:
                if winning_number == my_number:
                    round_points += 1

        for j in range(card_id + 1, card_id + round_points + 1):
            input_text.append(original_input_text[j])
            total_card_number += 1

        del input_text[0]

        # Loggging only increments of 10'000 in size
        if len(input_text) % 10000 == 0:
            print('length of input_text: ', len(input_text))

    print('total_card_number: ', total_card_number)

    return total_card_number


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_4_test_input.txt")
    assert 30 == aoc_day_4b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_4_actual_input.txt")
    aoc_day_4b(parsed_file)



from utils import parse_text_file_by_line


def aoc_day_15a(input_text):
    input_list = input_text[0].split(',')
    total_sum = 0

    for hash_word in input_list:
        hash_sum = 0
        for character in hash_word:
            ascii_int = ord(character)
            hash_sum = ((hash_sum + ascii_int) * 17) % 256
        total_sum += hash_sum

    print('total_sum: ', total_sum)

    return total_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_15_test_input.txt")
    assert 1320 == aoc_day_15a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_15_actual_input.txt")
    aoc_day_15a(parsed_file)
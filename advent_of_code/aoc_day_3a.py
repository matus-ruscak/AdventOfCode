from utils import parse_text_file_by_line
import string


def aoc_day_3a(input_text_file):
    all_letters = string.ascii_lowercase + string.ascii_uppercase
    all_letters_list = [i for i in all_letters]
    all_letters_enumerated_generator = enumerate(all_letters_list, start=1)
    all_letters_enumerated = [i for i in all_letters_enumerated_generator]
    print(type(all_letters_enumerated))

    total_sum = 0

    for code in input_text_file:
        half_length = int(len(code) / 2)
        first_half = code[:half_length]
        second_half = code[half_length:]

        duplicates = set()
        code_sum = 0
        for letter in first_half:
            if letter in second_half:
                duplicates.add(letter)

        for duplicated_letter in duplicates:
            for enumerated_letter in all_letters_enumerated:
                if duplicated_letter == enumerated_letter[1]:
                    code_sum += enumerated_letter[0]

        total_sum += code_sum

    return total_sum


if __name__ == '__main__':
    parsed_test_file = parse_text_file_by_line("../input/aoc_day_3_test_input.txt")
    assert 157 == aoc_day_3a(parsed_test_file)

    parsed_test_file = parse_text_file_by_line("../input/aoc_day_3_actual_input.txt")
    total_duplicate_sum = aoc_day_3a(parsed_test_file)
    print(total_duplicate_sum)











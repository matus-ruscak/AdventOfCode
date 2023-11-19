from utils import parse_text_file_by_line, return_enumerated_alphabet
from difflib import SequenceMatcher


def aoc_day_3b(input_text_file):
    all_letters_enumerated = return_enumerated_alphabet()
    total_sum = 0

    elf_groups = [tuple(input_text_file[i:i+3]) for i in range(0, len(input_text_file), 3)]
    for elf_group in elf_groups:
        elf_group_sum = 0
        match_1_2 = ''.join(set(elf_group[0]).intersection(elf_group[1]))
        match_1_2_3 = ''.join(set(match_1_2).intersection(elf_group[2]))
        for enumerated_letter in all_letters_enumerated:
            if match_1_2_3 == enumerated_letter[1]:
                elf_group_sum += enumerated_letter[0]
        total_sum += elf_group_sum

    print('total_sum: ', total_sum)
    return total_sum


if __name__ == '__main__':
    parsed_test_file = parse_text_file_by_line("../input/aoc_day_3_test_input.txt")
    assert aoc_day_3b(parsed_test_file) == 70

    parsed_test_file = parse_text_file_by_line("../input/aoc_day_3_actual_input.txt")
    aoc_day_3b(parsed_test_file)










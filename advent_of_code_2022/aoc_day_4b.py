from utils import parse_text_file_by_line


def aoc_day_4a(input_text_file):
    elf_pairs = []
    for item in input_text_file:
        elf_pairs.append(item.split(sep=','))

    total_overlap_count = 0

    for elf_pair in elf_pairs:
        start_index_elf_1 = int(elf_pair[0].split(sep='-')[0])
        end_index_elf_1 = int(elf_pair[0].split(sep='-')[1])
        start_index_elf_2 = int(elf_pair[1].split(sep='-')[0])
        end_index_elf_2 = int(elf_pair[1].split(sep='-')[1])

        elf_1_str_sequence = set()
        for i in range(start_index_elf_1, end_index_elf_1 + 1):
            elf_1_str_sequence.add(i)

        elf_2_str_sequence = set()
        for i in range(start_index_elf_2, end_index_elf_2 + 1):
            elf_2_str_sequence.add(i)

        for elf_1_item in elf_1_str_sequence:
            if elf_1_item in elf_2_str_sequence:
                total_overlap_count += 1
                break

    print(total_overlap_count)
    return total_overlap_count


if __name__ == '__main__':
    #parsed_test_file = parse_text_file_by_line("input/aoc_day_4_test_input.txt")
    #assert 2 == aoc_day_4a(parsed_test_file)

    parsed_test_file = parse_text_file_by_line("input/aoc_day_4_actual_input.txt")
    aoc_day_4a(parsed_test_file)














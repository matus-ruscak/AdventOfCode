from utils import parse_text_file_by_line
import pprint


def return_box_id(hash_word):
    hash_sum = 0
    for character in hash_word:
        ascii_int = ord(character)
        hash_sum = ((hash_sum + ascii_int) * 17) % 256
    return hash_sum


def calculate_result_sum(box_dictionary):
    final_sum = 0
    for box, list_of_lenses in box_dictionary.items():
        for i in range(len(list_of_lenses)):
            final_sum += (box+1) * (i+1) * int(list_of_lenses[i][1])

    print('FINAL SUM: ', final_sum)
    return final_sum


def aoc_day_15b(input_text):
    input_list = input_text[0].split(',')

    # dictionary of tuples, e.g. {0: [(rn, 2), (cn, 1)]
    box_dict = {}

    for hash_word in input_list:
        if ('-' not in hash_word) and ('=' not in hash_word):
            continue
        elif '-' in hash_word:
            label = hash_word.split('-')[0]
            operation = 'remove'
            focal_length = None
        else:
            label = hash_word.split('=')[0]
            focal_length = hash_word.split('=')[1]
            operation = 'add'

        box_id = return_box_id(label)

        if operation == 'add':
            if box_id not in box_dict:
                box_dict[box_id] = [(label, focal_length)]
            else:
                new_lense_list = []
                replaced = False
                for lense in box_dict.get(box_id):
                    if lense[0] == label:
                        new_lense_list.append((label, focal_length))
                        replaced = True
                    else:
                        new_lense_list.append(lense)
                if not replaced:
                    new_lense_list.append((label, focal_length))
                box_dict[box_id] = new_lense_list

        if operation == 'remove':
            if box_id in box_dict:
                new_lense_list = []
                for lense in box_dict.get(box_id):
                    if lense[0] != label:
                        new_lense_list.append(lense)
                box_dict[box_id] = new_lense_list

    pprint.pprint(box_dict)

    result_sum = calculate_result_sum(box_dict)

    return result_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_15_test_input.txt")
    assert 145 == aoc_day_15b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_15_actual_input.txt")
    aoc_day_15b(parsed_file)

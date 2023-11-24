import string


def parse_text_file_by_line(file_path):
    with open(file_path) as f:
        lines = [line.rstrip() for line in f]
        return lines


def parse_text_file_by_line_no_strip(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()
        return lines


def split_input_text_into_2_parts(input_text_file):
    part_1 = []
    part_2 = []
    after_delimiter = False
    for i in input_text_file:
        if i == '':
            after_delimiter = True
        elif after_delimiter:
            part_1.append(i)
        else:
            part_2.append(i)
    return part_1, part_2


def split_generator(sequence, sep):
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(val)
    yield chunk


def return_split_list(sequence, sep):
    return_list = []
    for i in split_generator(sequence, sep):
        return_list.append(i)
    return return_list


def return_enumerated_alphabet():
    all_letters = string.ascii_lowercase + string.ascii_uppercase
    all_letters_list = [i for i in all_letters]
    all_letters_enumerated_generator = enumerate(all_letters_list, start=1)
    all_letters_enumerated = [i for i in all_letters_enumerated_generator]

    return all_letters_enumerated

import string


def parse_text_file_by_line(file_path):
    with open(file_path) as f:
        lines = [line.rstrip() for line in f]
        return lines


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

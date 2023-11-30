from utils import parse_text_file_by_line
import re


def aoc_day_7a_calculate_file_size_per_dictionary(input_text_file):
    result_dictionary = {}
    for i in range(len(input_text_file)):
        current_line = input_text_file[i]
        print('current_line')
        dir_level = round(current_line.find("-") / 2) if "dir" in current_line and "/" not in current_line else None
        print('dir_level: ', dir_level)
        print('current_line.find("-"): ', current_line.find("-"))
        current_level = round(current_line.find("-") / 2)

        dir_label = current_line[dir_level * 2 + 2:].split(" ")[0] if dir_level else None
        if dir_label:
            result_dictionary[dir_label+str(i)] = 0

        # Otherwise it's a file
        else:
            if i >= 1:
                size = int(re.search('size=(.*)\)', current_line).group(1))
                already_used_level = current_level
                for j in reversed(range(0, i)):
                    upstream_line = input_text_file[j]
                    upstream_dir_level = round(upstream_line.find("-") / 2) if "dir" in upstream_line else None
                    upstream_dir_label = upstream_line[upstream_dir_level * 2 + 2:].split(" ")[0] if upstream_dir_level else None
                    if upstream_dir_label:
                        if upstream_dir_level > current_level:
                            pass
                        else:
                            if already_used_level > upstream_dir_level:
                                result_dictionary[upstream_dir_label+str(j)] = result_dictionary[upstream_dir_label+str(j)] + size
                                already_used_level = upstream_dir_level

    print('result_dictionary: ', result_dictionary)
    return result_dictionary


def aoc_day_7a_parse_commands_into_table(input_text_file):
    result_list_structure = []
    level = 0
    for command in input_text_file:
        if "cd" in command:
            if "/" in command:
                result_line = "- / (dir)"
                result_list_structure.append(result_line)
                level += 1
            elif ".." in command:
                level += -1
            else:
                dir_name = command.replace("$ cd ", "")
                result_line = 2 * level * " " + f"- {dir_name} (dir)"
                result_list_structure.append(result_line)
                level += 1
        elif command.split(" ")[0].isnumeric():
            file_size = command.split(" ")[0]
            file_name = command.split(" ")[1]
            result_line = 2 * level * " " + f"- {file_name} (file, size={file_size})"
            result_list_structure.append(result_line)

    return result_list_structure


def find_smallest_dictionary_to_free_up_space(folder_sizes: dict, total_occupied_size: int):
    total_size = 70000000
    required_size = 30000000

    current_free_size = total_size - total_occupied_size
    required_to_be_deleted = required_size - current_free_size

    usable_folders_for_deletion = []
    for folder_name, folder_size in folder_sizes.items():
        if folder_size >= required_to_be_deleted:
            usable_folders_for_deletion.append(folder_size)
    usable_folders_for_deletion.sort()
    size_of_the_smallest_applicable_folder = min(usable_folders_for_deletion)

    print('size_of_the_smallest_applicable_folder: ', size_of_the_smallest_applicable_folder)

    return size_of_the_smallest_applicable_folder


def calculate_total_file_size(folder_structure):
    total_file_size = 0
    for i in range(len(folder_structure)):
        current_line = folder_structure[i]
        if 'file' in current_line:
            size = int(re.search('size=(.*)\)', current_line).group(1))
            total_file_size += size

    print('total occupied size: ', total_file_size)
    return total_file_size


if __name__ == '__main__':
    # Correct answer -> 3636703

    # Test
    # parsed_test_file = parse_text_file_by_line("../input/aoc_day_7_test_input_commands.txt")
    # folder_structure = aoc_day_7a_parse_commands_into_table(parsed_test_file)
    # folder_size_dictionary = aoc_day_7a_calculate_file_size_per_dictionary(folder_structure)
    # total_file_size = calculate_total_file_size(folder_structure)
    # assert find_smallest_dictionary_to_free_up_space(folder_size_dictionary, total_file_size) == 24933642


    parsed_test_file = parse_text_file_by_line("input/aoc_day_7_actual_input_commands.txt")
    folder_structure = aoc_day_7a_parse_commands_into_table(parsed_test_file)
    folder_size_dictionary = aoc_day_7a_calculate_file_size_per_dictionary(folder_structure)
    total_file_size = calculate_total_file_size(folder_structure)
    find_smallest_dictionary_to_free_up_space(folder_size_dictionary, total_file_size)

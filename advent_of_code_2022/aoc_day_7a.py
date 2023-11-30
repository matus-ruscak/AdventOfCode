from utils import parse_text_file_by_line
import re


def aoc_day_7a_calculate_file_size(input_text_file):
    result_dictionary = {}
    for i in range(len(input_text_file)):
        current_line = input_text_file[i]
        dir_level = round(current_line.find("-") / 2) if "dir" in current_line and "/" not in current_line else None
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

    # Sum all which have size at most 100000
    result_value = 0
    for directory, size in result_dictionary.items():
        if size <= 100000:
            result_value += size

    return result_value


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


if __name__ == '__main__':

    parsed_test_file = parse_text_file_by_line("../input/aoc_day_7_test_input_commands.txt")
    folder_structure = aoc_day_7a_parse_commands_into_table(parsed_test_file)

    assert aoc_day_7a_calculate_file_size(folder_structure) == 95437

    parsed_test_file = parse_text_file_by_line("../input/aoc_day_7_actual_input_commands.txt")
    folder_structure = aoc_day_7a_parse_commands_into_table(parsed_test_file)
    print('result size: ', aoc_day_7a_calculate_file_size(folder_structure))

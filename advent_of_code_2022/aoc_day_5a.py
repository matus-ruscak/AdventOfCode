from utils import parse_text_file_by_line_no_strip, split_input_text_into_2_parts


def aoc_day_5a(input_text_file):

    instructions, containers = split_input_text_into_2_parts(input_text_file)

    container_labels = containers[len(containers)-1].replace(' ', '')
    number_of_containers = int(container_labels[len(container_labels)-1])
    print('number_of_containers: ', number_of_containers)

    container_lines = containers[:len(containers)-1]
    full_container_length = number_of_containers * 3 + (number_of_containers - 1)
    print('full_container_length: ', full_container_length)

    modified_container_lines = []
    for container_line in container_lines:
        container_line = container_line.ljust(full_container_length)
        modified_container_line = []
        for i in range(0, int(number_of_containers)):
            if i == 0:
                step = i*3
            else:
                step = i*3 + i

            container_content = container_line[step:step + 3]

            if container_content == '   ':
                modified_container_line.append(None)
            else:
                modified_container_line.append(container_content[1])
        modified_container_lines.append(modified_container_line)

    # Create list structure
    transformed_containers = []
    for i in range(number_of_containers):
        transformed_containers.append([])

    # The first item in the list is the top on in the container
    for i in range(0, len(modified_container_lines)):
        for j in range(0, len(modified_container_lines[i])):
            if modified_container_lines[i][j] is not None:
                transformed_containers[j].append(modified_container_lines[i][j])

    parsed_instructions = []
    for instruction in instructions:
        instruction = instruction.replace('move ', '').replace(' from ', '-').replace(' to ', '-')
        parsed_instructions.append(instruction)

    for instruction in parsed_instructions:
        num_containers_to_be_moved = int(instruction.split('-')[0])
        container_from = int(instruction.split('-')[1]) - 1
        container_to = int(instruction.split('-')[2]) - 1

        for _ in range(num_containers_to_be_moved):
            transformed_containers[container_to].insert(0, transformed_containers[container_from][0])
            transformed_containers[container_from].pop(0)

    # Collect top items
    result_string = ""
    for container in transformed_containers:
        result_string += container[0]

    print('RESULT STRING: ', result_string)
    return result_string


if __name__ == '__main__':

    parsed_test_file = parse_text_file_by_line_no_strip("../input/aoc_day_5_test_input.txt")
    assert aoc_day_5a(parsed_test_file) == 'CMZ'

    parsed_test_file = parse_text_file_by_line_no_strip("../input/aoc_day_5_actual_input.txt")
    actual_result = aoc_day_5a(parsed_test_file)













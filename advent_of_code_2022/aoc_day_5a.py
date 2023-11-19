from utils import parse_text_file_by_line_no_strip
import numpy as np

def aoc_day_5a(input_text_file):
    containers = []
    instructions = []
    after_delimiter = False
    for i in input_text_file:
        if i == '':
            after_delimiter = True
        elif after_delimiter:
            instructions.append(i)
        else:
            containers.append(i)

    #print(containers)
    #print(instructions)

    container_labels = containers[len(containers)-1].replace(' ', '')
    number_of_containers = int(container_labels[len(container_labels)-1])
    #print('number_of_containers: ', number_of_containers)

    container_lines = containers[:len(containers)-1]
    #print(container_lines)

    modified_container_lines = []
    for container_line in container_lines:
        #print('container_line: ', container_line)
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

    max_container_items = len(modified_container_lines)

    container_array = np.zeros((number_of_containers, max_container_items), str)
    print(container_array)

    print('modified_container_lines: ', modified_container_lines)

    transformed_list = []

    for i in range(0, len(modified_container_lines)):
        for j in range(0, len(modified_container_lines[i])):
            print(modified_container_lines[i][j])


if __name__ == '__main__':
    parsed_test_file = parse_text_file_by_line_no_strip("../input/aoc_day_5_test_input.txt")

    aoc_day_5a(parsed_test_file)













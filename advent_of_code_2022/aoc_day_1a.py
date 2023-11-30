from utils import parse_text_file_by_line, return_split_list

if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("input/aoc_day_1_actual_input.txt")

    result_list = return_split_list(parsed_file, '')

    summed_result_list = []
    for i in result_list:
        total_sum = 0
        for j in i:
            total_sum += int(j)
        summed_result_list.append(total_sum)

    summed_result_list.sort()

    print(max(summed_result_list))



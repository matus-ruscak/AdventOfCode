from utils import parse_text_file_by_line, return_split_list


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("input/aoc_day_1_actual_input.txt")

    result_list = return_split_list(parsed_file, '')

    summed_result_list = []
    for i in result_list:
        sum = 0
        for j in i:
            sum += int(j)
        summed_result_list.append(sum)

    summed_result_list.sort(reverse=True)

    top_three_sum = 0
    for i in summed_result_list[0:3]:
        top_three_sum += i

    print(top_three_sum)



from utils import parse_text_file_by_line
import re

symbols = ['#', '+', '-', '=', '$', '@', '%', '/', '*', '&']
extended_list_of_symbols = ['#', '+', '-', '=', '$', '@', '%', '/', '*', '&', '.']

def aoc_day_3a(input_text):
    valid_numbers = []

    for i in range(len(input_text)):
    # for i in range(84):
        print(i)
        line = input_text[i]
        print('line: ', line)
        numbers_in_line = re.findall(r'\d+', line)
        print('numbers_in_line: ', numbers_in_line)
        for number_in_line in numbers_in_line:
            index = None
            print('number_in_line: ', number_in_line)
            for extended_symbol in extended_list_of_symbols:
                for ext_symbol_reversed in extended_symbol:
                    if extended_symbol + number_in_line + ext_symbol_reversed in line:
                        index = line.find(extended_symbol + number_in_line + ext_symbol_reversed)
                        index += 1
                        print('set index on line 25: ', index)
                        break
            if index is None:
                for extended_symbol in extended_list_of_symbols:
                    if number_in_line + extended_symbol in line:
                        init_index = line.find(number_in_line + extended_symbol)
                        print(line[init_index-1])
                        if not line[init_index-1].isnumeric():
                            index = init_index
                        print('set index on line 31: ', index)
            if index is None:
                for extended_symbol in extended_list_of_symbols:
                    if extended_symbol + number_in_line in line:
                        index = line.find(extended_symbol + number_in_line)
                        index += 1
                        print('set index on line 37: ', index)

            print('index: ', index)
            already_added = False
            if (index > 0) and (line[index - 1] in symbols):
                print('ADDING number: ', number_in_line, ' on line 22')
                valid_numbers.append(int(number_in_line))
                already_added = True
            if (not already_added) and (len(line) > (index + len(number_in_line))):
                print('len(line): ', len(line))
                print('index + len(number_in_line): ', index + len(number_in_line))
                print('line[index + len(number_in_line)]: ', line[index + len(number_in_line)])
                if line[index + len(number_in_line)] in symbols:
                    print('ADDING number: ', number_in_line, ' on line 30')
                    valid_numbers.append(int(number_in_line))
                    already_added = True
            if (not already_added) and (i > 0):
                previous_line = input_text[i - 1]
                print('i: ', i)
                print('previous_line: ', previous_line)
                for symbol in symbols:
                    if not already_added:
                        index_floored = 1 if index == 0 else index
                        print('index_floored - 1: ', index_floored - 1)
                        print('index_floored-1 + len(number_in_line) + 1: ', index_floored-1 + len(number_in_line) + 1)
                        print('relevant part of previous line: ', previous_line[index_floored - 1: index_floored + len(number_in_line) + 1])
                        if symbol in previous_line[index_floored - 1: index_floored + len(number_in_line) + 1]:
                            print('ADDING number: ', number_in_line, ' on line 42')
                            valid_numbers.append(int(number_in_line))
                            already_added = True

            if not already_added and (i < len(input_text) - 1):
                next_line = input_text[i + 1]
                print('next_line: ', next_line)
                for symbol in symbols:
                    if not already_added:
                        if index == 0:
                            if symbol in next_line[0: len(number_in_line) + 1]:
                                print('ADDING number: ', number_in_line, ' on line 78')
                                valid_numbers.append(int(number_in_line))
                                already_added = True
                        else:
                            if symbol in next_line[index - 1: index + len(number_in_line) + 1]:
                                print('ADDING number: ', number_in_line, ' on line 83')
                                valid_numbers.append(int(number_in_line))
                                already_added = True
            print('')
            print('')

    print('valid_numbers: ', valid_numbers)

    total_sum = 0
    for i in valid_numbers:
        total_sum += int(i)

    print('total_sum: ', total_sum)
    return total_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_3_test_input.txt")
    #assert 4361 == aoc_day_3a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_3_actual_input.txt")
    aoc_day_3a(parsed_file)
    # 288092 too low
    # 292244 too low
    # 496160 WRONG
    # 540655 WRONG
    # 469498 WRONG
    # WRONG 540428
    # 540613 WRONG
    # 494322
    # 540588

    # Problematic lines - 82 and 8

    # 6 is missing
    # 563 shouldn't be there

    # Parse special symbols
    # symbol_set = set()
    # for line in parsed_file:
    #     for character in line:
    #         if character not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
    #             symbol_set.add(character)
    # print('symbol_set: ', symbol_set)



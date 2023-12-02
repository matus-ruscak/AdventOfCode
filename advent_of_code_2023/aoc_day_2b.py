from utils import parse_text_file_by_line
import re


def aoc_day_2b(input_text):
    result_list = []

    for game in input_text:
        game_dictionary = {'red': 0, 'green': 0, 'blue': 0}
        game_id = re.search('Game (.*):', game).group(1)
        rounds_string = game.replace(f'Game {game_id}: ', '')
        rounds = rounds_string.split(';')
        rounds_stripped = [round.strip() for round in rounds]
        for round in rounds_stripped:
            for cube in round.split(', '):
                cube_number = int(cube.split(' ')[0].strip())
                cube_color = cube.split(' ')[1].strip()
                if cube_number > game_dictionary[cube_color]:
                    game_dictionary[cube_color] = cube_number

        game_result = game_dictionary['red'] * game_dictionary['blue'] * game_dictionary['green']
        result_list.append(game_result)


    total_sum = 0
    for i in result_list:
        total_sum += i

    print('total_sum: ', total_sum)

    return total_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_2_test_input.txt")
    assert 2286 == aoc_day_2b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_2_actual_input.txt")
    aoc_day_2b(parsed_file)


from utils import parse_text_file_by_line
import re

limits = {'red': 12,
          'green': 13,
          'blue': 14}


def aoc_day_2a(input_text):
    invalid_games = set()
    all_games = set()

    for game in input_text:
        game_id = re.search('Game (.*):', game).group(1)
        rounds_string = game.replace(f'Game {game_id}: ', '')
        rounds = rounds_string.split(';')
        rounds_stripped = [round.strip() for round in rounds]
        for round in rounds_stripped:
            for cube in round.split(', '):
                cube_number = int(cube.split(' ')[0].strip())
                cube_color = cube.split(' ')[1].strip()
                if cube_number > limits[cube_color]:
                    invalid_games.add(game_id)

        all_games.add(game_id)

    valid_games = all_games.difference(invalid_games)

    total_sum = 0
    for i in list(valid_games):
        total_sum += int(i)

    print('total_sum: ', total_sum)

    return total_sum


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_2_test_input.txt")
    assert 8 == aoc_day_2a(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_2_actual_input.txt")
    aoc_day_2a(parsed_file)


from utils import parse_text_file_by_line, return_split_list

# A - player 1 - ROCK
# B - player 1 - PAPER
# c - player 1 - SCISSORS
# X - player 2 - ROCK
# Y - player 2 - PAPER
# Z - player 2 - SCISSORS

# X - I need to LOSE
# Y - I need to DRAW
# Z - I need to WIN

rock = {'hand_score': 1, 'player_1': 'A', 'to_win': 'paper', 'to_lose': 'scissors'}
paper = {'hand_score': 2, 'player_1': 'B', 'to_win': 'scissors', 'to_lose': 'rock'}
scissors = {'hand_score': 3, 'player_1': 'C', 'to_win': 'rock', 'to_lose': 'paper'}

hand_dictionary = {'rock': rock, 'paper': paper, 'scissors': scissors}

winning_combinations = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
draw_combinations = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
lose_combinations = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]

round_score_all = {'X': 0, 'Y': 3, 'Z': 6}


def aoc_day_2b(tuple_list_of_games):
    total_score = 0

    for game_round in tuple_list_of_games:
        hand_score = 0
        round_score = 0

        round_score = round_score_all[game_round[1]]

        for hand_type, content in hand_dictionary.items():
            if game_round[0] == content['player_1']:
                player_1_hand_type = hand_type

        if game_round[1] == 'Y':
            hand_score = hand_dictionary[player_1_hand_type]['hand_score']
            required_hand_type = None
        elif game_round[1] == 'X':
            required_hand_type = hand_dictionary[player_1_hand_type]['to_lose']
        else :
            required_hand_type = hand_dictionary[player_1_hand_type]['to_win']

        if required_hand_type:
            hand_score = hand_dictionary[required_hand_type]['hand_score']

        total_score += round_score + hand_score

    return total_score


if __name__ == '__main__':
    parsed_test_file = parse_text_file_by_line("input/aoc_day_2_test_input.txt")
    list_of_test_tuples = [(i.rsplit(' ')[0], i.rsplit(' ')[1]) for i in parsed_test_file]
    result_test_score = aoc_day_2b(list_of_test_tuples)

    assert result_test_score == 12

    parsed_actual_file = parse_text_file_by_line("input/aoc_day_2_actual_input.txt")
    list_of_actual_tuples = [(i.rsplit(' ')[0], i.rsplit(' ')[1]) for i in parsed_actual_file]
    result_actual_score = aoc_day_2b(list_of_actual_tuples)
    print(result_actual_score)







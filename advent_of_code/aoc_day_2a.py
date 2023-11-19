from utils import parse_text_file_by_line, return_split_list

# A - player 1 - ROCK
# B - player 1 - PAPER
# c - player 1 - SCISSORS
# X - player 2 - ROCK
# Y - player 2 - PAPER
# Z - player 2 - SCISSORS

rock = {'hand_score': 1, 'player_1': 'A', 'player_2': 'X'}
paper = {'hand_score': 2, 'player_1': 'B', 'player_2': 'Y'}
scissors = {'hand_score': 3, 'player_1': 'C', 'player_2': 'Z'}

hand_dictionary = {'rock': rock, 'paper': paper, 'scissors': scissors}


def aoc_day_2a(tuple_list_of_games):
    total_score = 0

    for game_round in tuple_list_of_games:
        hand_score = 0
        round_score = 0
        for hand_type, content in hand_dictionary.items():
            if content['player_2'] == game_round[1]:
                hand_score = content['hand_score']
                player_2_hand = hand_type

            if content['player_1'] == game_round[0]:
                player_1_hand = hand_type

        if player_1_hand == player_2_hand:
            round_score = 3
        elif player_1_hand == 'rock':
            if player_2_hand == 'paper':
                round_score = 6
            else:
                round_score = 0
        elif player_1_hand == 'paper':
            if player_2_hand == 'rock':
                round_score = 0
            else:
                round_score = 6
        elif player_1_hand == 'scissors':
            if player_2_hand == 'paper':
                round_score = 0
            else:
                round_score = 6
        total_score += hand_score + round_score

    return total_score


if __name__ == '__main__':
    parsed_test_file = parse_text_file_by_line("../input/aoc_day_2_test_input.txt")
    list_of_test_tuples = [(i.rsplit(' ')[0], i.rsplit(' ')[1]) for i in parsed_test_file]
    result_test_score = aoc_day_2a(list_of_test_tuples)

    assert result_test_score == 15

    parsed_actual_file = parse_text_file_by_line("../input/aoc_day_2_actual_input.txt")
    list_of_actual_tuples = [(i.rsplit(' ')[0], i.rsplit(' ')[1]) for i in parsed_actual_file]
    result_actual_score = aoc_day_2a(list_of_actual_tuples)
    print(result_actual_score)







from utils import parse_text_file_by_line

card_rank = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}

five_of_kind = 6
four_of_kind = 5
full_house = 4
three_of_kind = 3
two_pair = 2
one_pair = 1


def calculate_character_count(card):
    character_count = {}
    for i in card:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
    return character_count


def calculate_main_card_score(character_count):
    card_score = 0
    if 5 in character_count.values():
        card_score += five_of_kind * 10 ** 20
    elif 4 in character_count.values():
        card_score += four_of_kind * 10 ** 19
    elif (3 in character_count.values()) and (2 in character_count.values()) and (len(character_count) == 2):
        card_score += full_house * 10 ** 18
    elif (3 in character_count.values()) and (len(character_count) == 3):
        card_score += three_of_kind * 10 ** 17
    elif (2 in character_count.values()) and (len(character_count) == 3):
        card_score += two_pair * 10 ** 16
    elif (2 in character_count.values()) and (len(character_count) == 4):
        card_score += one_pair * 10 ** 15

    return card_score


def aoc_day_7b(input_text):
    card_dict = {}
    for hand in input_text:
        card_bid = hand.split(' ')
        card_dict[card_bid[0]] = int(card_bid[1])

    card_score_bid_dict = {}

    for card, bid in card_dict.items():
        card_score_bid_dict[card] = {}
        character_count = calculate_character_count(card)

        # Full combinations - modify for Joker
        if 'J' in character_count.keys():
            joker_indices = [i for i, ltr in enumerate(card) if ltr == 'J']
            replacement_letters = [i for i in card_rank.keys() if i != 'J']
            card_score = 0
            for i in range(len(joker_indices)):
                # Single replacement
                if i == 0:
                    for replacement_letter in replacement_letters:
                        rewritten_card = card[0:joker_indices[i]] + replacement_letter + card[joker_indices[i]+1:]
                        rewritten_card_char_count = calculate_character_count(rewritten_card)
                        local_card_score = calculate_main_card_score(rewritten_card_char_count)
                        if local_card_score > card_score:
                            card_score = local_card_score
                # Double replacement
                if i == 1:
                    for replacement_letter in replacement_letters:
                        for replacement_letter_2 in replacement_letters:
                            rewritten_card = card[0:joker_indices[0]] + replacement_letter + card[joker_indices[0] + 1:joker_indices[1]] + replacement_letter_2 + card[joker_indices[1]+1:]
                            rewritten_card_char_count = calculate_character_count(rewritten_card)
                            local_card_score = calculate_main_card_score(rewritten_card_char_count)
                            if local_card_score > card_score:
                                card_score = local_card_score
                # Triple replacement
                if i == 2:
                    for replacement_letter in replacement_letters:
                        for replacement_letter_2 in replacement_letters:
                            for replacement_letter_3 in replacement_letters:
                                rewritten_card = card[0:joker_indices[0]] + replacement_letter + card[joker_indices[0] + 1:joker_indices[1]] + replacement_letter_2 + card[joker_indices[1]+1:joker_indices[2]] + replacement_letter_3 + card[joker_indices[2]+1:]
                                rewritten_card_char_count = calculate_character_count(rewritten_card)
                                local_card_score = calculate_main_card_score(rewritten_card_char_count)
                                if local_card_score > card_score:
                                    card_score = local_card_score
                # Quadruple replacement
                if i == 3:
                    for replacement_letter in replacement_letters:
                        for replacement_letter_2 in replacement_letters:
                            for replacement_letter_3 in replacement_letters:
                                for replacement_letter_4 in replacement_letters:
                                    rewritten_card = card[0:joker_indices[0]] + replacement_letter + card[joker_indices[0] + 1:joker_indices[1]] + replacement_letter_2 + card[joker_indices[1] + 1:joker_indices[2]] + replacement_letter_3 + card[joker_indices[2] + 1:joker_indices[3]] + replacement_letter_4 + card[joker_indices[3]+1:]
                                    rewritten_card_char_count = calculate_character_count(rewritten_card)
                                    local_card_score = calculate_main_card_score(rewritten_card_char_count)
                                    if local_card_score > card_score:
                                        card_score = local_card_score

                # Five char replacement
                if i == 4:
                    for replacement_letter in replacement_letters:
                        for replacement_letter_2 in replacement_letters:
                            for replacement_letter_3 in replacement_letters:
                                for replacement_letter_4 in replacement_letters:
                                    for replacement_letter_5 in replacement_letters:
                                        rewritten_card = replacement_letter + replacement_letter_2 + replacement_letter_3 + replacement_letter_4 + replacement_letter_5
                                        rewritten_card_char_count = calculate_character_count(rewritten_card)
                                        local_card_score = calculate_main_card_score(rewritten_card_char_count)
                                        if local_card_score > card_score:
                                            card_score = local_card_score

        else:
            card_score = calculate_main_card_score(character_count)

        # Single character
        for i in range(len(card)):
            card_score += card_rank[card[i]] * 10 ** (10 - 2*i)

        card_score_bid_dict[card]['score'] = card_score
        card_score_bid_dict[card]['bid'] = bid

    # Sort the dictionary
    sorted_card_score_bid_dict = {k: v for k, v in sorted(card_score_bid_dict.items(), key=lambda item: item[1]['score'])}

    # Result calculation
    result_list = []
    for card, details in sorted_card_score_bid_dict.items():
        result_list.append(details['bid'])

    # Total score
    total_score = 0
    for i in range(len(result_list)):
        total_score += (i+1) * result_list[i]

    print('total_score: ', total_score)

    return total_score


if __name__ == '__main__':
    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_7_test_input.txt")
    assert 5905 == aoc_day_7b(parsed_file)

    parsed_file = parse_text_file_by_line("../advent_of_code_2023/input/aoc_day_7_actual_input.txt")
    aoc_day_7b(parsed_file)

    #

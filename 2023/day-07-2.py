import math
import re

with open('day-07.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile(r'^(.+) (\d+)$')

two_pattern = re.compile(r'.*(.)\1{1}.*')
two_and_two_pattern = re.compile(r'.*(.)\1.*(.)\2.*')
full_house_pattern = re.compile(r'(.*(.)\2.*(.)\3\3.*|.*(.)\4\4.*(.)\5.*)')
three_pattern = re.compile(r'.*(.)\1{2}.*')
four_pattern = re.compile(r'.*(.)\1{3}.*')
five_pattern = re.compile(r'.*(.)\1{4}.*')

card_scores = {'A': 12, 'K': 11, 'Q': 10, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2,
               '2': 1}


def count_max_single_occurrence(cards_sorted):
    if five_pattern.match(cards_sorted):
        return 5
    if four_pattern.match(cards_sorted):
        return 4
    if three_pattern.match(cards_sorted):
        return 3
    if two_pattern.match(cards_sorted):
        return 2

    if len(cards_sorted) == 0:
        return 0

    return 1


def calc_hand_type_score(cards):
    cards_sorted = ''.join(list(filter(lambda c: c != 'J', sorted(cards))))
    jokers = len(cards) - len(cards_sorted)
    max_single_occurrence = count_max_single_occurrence(cards_sorted)

    print(f'{cards} -> {jokers} -> {cards_sorted} -> {max_single_occurrence}')

    max_single_occurrence_with_jokers = max_single_occurrence + jokers
    if max_single_occurrence_with_jokers > 3:
        return max_single_occurrence_with_jokers + 1

    if full_house_pattern.match(cards_sorted):
        return 4
    if two_and_two_pattern.match(cards_sorted) and jokers == 1:
        return 4
    if max_single_occurrence_with_jokers == 3:
        return 3
    if two_and_two_pattern.match(cards_sorted):
        return 2
    if max_single_occurrence_with_jokers == 2:
        return 1
    return 0


def calc_cards_score(cards):
    score = 0
    for i in range(5):
        score += card_scores[cards[5 - i - 1]] * math.pow(13, i)

    return score


class Hand:

    def __init__(self, cards, bid):
        hand_type_score = int(calc_hand_type_score(cards))
        cards_score = int(calc_cards_score(cards))
        self.hand_type_score = hand_type_score
        self.cards = cards
        self.bid = bid
        self.score = hand_type_score * 1000000 + cards_score

    def __str__(self):
        return f'{self.cards} {self.hand_type_score} {self.score}'


def action():
    result = 0
    hands: list[Hand] = []
    for line in data:
        cards, bid = line_pattern.match(line).groups()
        hands.append(Hand(cards, int(bid)))

    hands.sort(key=lambda h: h.score)

    for i in range(len(hands)):
        print(hands[i])
        rank = i + 1
        result += rank * hands[i].bid

    return result


print(action())

# 253130504 too high
# 253029028 too high

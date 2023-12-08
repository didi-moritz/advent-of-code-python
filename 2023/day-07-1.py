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

card_scores = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1,
               '2': 0}


def calc_hand_type_score(cards):
    cards_sorted = ''.join(sorted(cards))

    if five_pattern.match(cards_sorted):
        return 6
    if four_pattern.match(cards_sorted):
        return 5
    if full_house_pattern.match(cards_sorted):
        return 4
    if three_pattern.match(cards_sorted):
        return 3
    if two_and_two_pattern.match(cards_sorted):
        return 2
    if two_pattern.match(cards_sorted):
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
        self.cards = cards
        self.bid = bid
        self.score = hand_type_score * 1000000 + cards_score

    def __str__(self):
        return f'{self.cards} {self.bid} {self.score}'


def action():
    result = 0
    hands: list[Hand] = []
    for line in data:
        cards, bid = line_pattern.match(line).groups()
        hands.append(Hand(cards, int(bid)))

    hands.sort(key=lambda h: h.score)

    for i in range(len(hands)):
        rank = i + 1
        result += rank * hands[i].bid

    return result


print(action())

# 250115194 too low

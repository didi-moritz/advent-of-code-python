import math
import re

with open('day-04.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile(r'^Card\ +\d+: (.*) \| (.*)$')
number_pattern = re.compile(r'\d+')


def score_of_card(winnings, tickets):
    winners = 0
    for ticket in tickets:
        if ticket in winnings:
            winners += 1

    if winners == 0:
        return 0

    return int(math.pow(2, winners - 1))


def action():
    result = 0
    for line in data:
        winnings, tickets = [number_pattern.findall(numbers) for numbers in line_pattern.match(line).groups()]
        result += score_of_card(winnings, tickets)

    return result


print(action())

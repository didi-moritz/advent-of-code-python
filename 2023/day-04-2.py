import math
import re

with open('day-04.data') as f:
    data = [line.rstrip('\n') for line in f]

count = len(data)

ticket_counts = [1 for i in range(count)]

line_pattern = re.compile(r'^Card\ +\d+: (.*) \| (.*)$')
number_pattern = re.compile(r'\d+')


def matches(winnings, tickets):
    winners = 0
    for ticket in tickets:
        if ticket in winnings:
            winners += 1

    return winners


def action():
    for i in range(count):
        line = data[i]
        winnings, tickets = [number_pattern.findall(numbers) for numbers in line_pattern.match(line).groups()]
        matching_tickets = matches(winnings, tickets)
        for j in range(i + 1, i + matching_tickets + 1):
            if j < count:
                ticket_counts[j] += ticket_counts[i]

    result = 0
    for i in range(count):
        result += ticket_counts[i]

    return result


print(action())

import math
import re

with open('day-08.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile(r'^(.+) = \((.+), (.+)\)$')


def action():
    mapping = {'L': {}, 'R': {}}

    directions = data[0]

    for i in range(2, len(data)):
        line = data[i]
        key, left, right = line_pattern.match(line).groups()
        mapping['L'][key] = left
        mapping['R'][key] = right

    i = 0
    current = 'AAA';
    while current != 'ZZZ':
        direction = directions[i % len(directions)]
        current = mapping[direction][current]
        i += 1

    return i


print(action())

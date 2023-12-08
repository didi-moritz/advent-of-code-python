import math
import re

with open('day-08.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile(r'^(.+) = \((.+), (.+)\)$')

mapping = {'L': {}, 'R': {}}

directions = data[0]


def full_move(node):
    for dir in directions:
        node = mapping[dir][node]

    return node


def action():
    for i in range(2, len(data)):
        line = data[i]
        key, left, right = line_pattern.match(line).groups()
        mapping['L'][key] = left
        mapping['R'][key] = right

    nodes = []

    all_nodes = mapping['L'].keys()

    full_mapping = {}

    for node in all_nodes:
        full_mapping[node] = full_move(node)

    for node in all_nodes:
        if node[2] == 'A':
            nodes.append(node)

    moves = {}

    for node in nodes:
        orig_node = node
        count = 0
        while node[2] != 'Z':
            node = full_mapping[node]
            count += 1

        moves[orig_node] = count

    return math.lcm(*moves.values()) * len(directions)


print(action())

# 35575074889 too low

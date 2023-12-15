import re

with open('day-14.data') as f:
    data = [line.rstrip('\n') for line in f]

part_pattern = re.compile('([.O]*)(#|$)')
stone_pattern = re.compile('O')


def rotate_pattern(pattern):
    new_pattern = []

    for x in range(len(pattern[0])):
        line = ''
        for y in range(len(pattern)):
            line += pattern[y][x]

        new_pattern.append(line)

    return new_pattern


def calc_load(line):
    i = 0
    load = 0
    length = len(line)
    while i < length:
        match = part_pattern.match(line, i)
        if not match:
            break

        group = match.groups()[0]
        stones = len(stone_pattern.findall(group))
        for j in range(stones):
            load += length - (i + j)

        i = match.regs[1][1] + 1

    return load


def action():
    pattern = rotate_pattern(data)

    result = 0
    for line in pattern:
        result += calc_load(line)

    return result


print(action())

# 88032 too low

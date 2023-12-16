import re

with open('day-14.data') as f:
    data = [line.rstrip('\n') for line in f]

part_pattern = re.compile('([.O]*)(#|$)')
stone_pattern = re.compile('O')


def rotate_pattern_ccw(pattern):
    new_pattern = []

    for x in range(len(pattern[0]) - 1, -1, -1):
        line = ''
        for y in range(len(pattern)):
            line += pattern[y][x]

        new_pattern.append(line)

    return new_pattern


def rotate_pattern_cw(pattern):
    new_pattern = []

    for x in range(len(pattern[0])):
        line = ''
        for y in range(len(pattern) - 1, -1, -1):
            line += pattern[y][x]

        new_pattern.append(line)

    return new_pattern


def roll_stones(line):
    i = 0
    length = len(line)
    while i < length:
        match = part_pattern.match(line, i)
        if not match:
            break

        group = match.groups()[0]
        if len(group) > 0:
            pos = match.regs[1][0]

            stones = len(stone_pattern.findall(group))
            replacement = ''
            for j in range(len(group)):
                replacement += 'O' if j < stones else '.'

            line = line[:pos] + replacement + line[pos + len(group):]

        i = match.regs[1][1] + 1

    return line


cache = {}


def get_cache_key(pattern):
    return '|'.join(pattern)


def roll_cycle(pattern, cache_key):
    global cache

    if not cache_key:
        cache_key = get_cache_key(pattern)

    if cache_key in cache:
        return cache[cache_key]

    for i in range(4):
        new_pattern = []
        for y in range(len(pattern)):
            new_pattern.append(roll_stones(pattern[y]))
        pattern = rotate_pattern_cw(new_pattern)

    result = (pattern, get_cache_key(pattern))

    cache[cache_key] = result
    return result


def calc_load(pattern):
    load = 0
    width = len(pattern[0])
    for line in pattern:
        for x in range(width):
            if line[x] == 'O':
                load += width - x

    return load


def find_cycles(start_cache_key):
    i = 0
    next_cache_key = ''
    while start_cache_key != next_cache_key:
        if not next_cache_key:
            next_cache_key = start_cache_key

        next_cache_key = cache[next_cache_key][1]
        i += 1

    return i


def action():
    pattern = rotate_pattern_ccw(data)

    cache_key = ''

    i = 0
    while True:
        pattern, next_cache_key = roll_cycle(pattern, cache_key)
        i += 1
        cache_key = next_cache_key
        if next_cache_key in cache:
            break

    cycles = find_cycles(next_cache_key)

    remaining = (1000000000 - i) % cycles

    next_cache_key = ''
    for j in range(remaining):
        pattern, next_cache_key = roll_cycle(pattern, next_cache_key)

    return calc_load(pattern)


print(action())

# 88032 too low

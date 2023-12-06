import re

with open('day-03.data') as f:
    data = [line.rstrip('\n') for line in f]

width = len(data[0])
height = len(data)

symbol_pattern = re.compile(r'[^\d.]')
digit_pattern = re.compile(r'\d')
number_pattern = re.compile(r'\d+')

found = [[' '] * width for y in range(height)]


def mark(x, y):
    found[y][x] = data[y][x]


def check_point(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return

    if digit_pattern.match(found[y][x]):
        return

    if digit_pattern.match(data[y][x]):
        mark(x, y)
        check_point(x - 1, y)
        check_point(x + 1, y)


def check_surroundings(symbol_x, symbol_y):
    for y in range(symbol_y - 1, symbol_y + 2):
        for x in range(symbol_x - 1, symbol_x + 2):
            check_point(x, y)


def action():
    result = 0
    for y in range(height):
        for x in range(width):
            if symbol_pattern.match(data[y][x]):
                check_surroundings(x, y)

    for y in range(height):
        line = ''.join(found[y])
        for number in number_pattern.findall(line):
            result += int(number)

    return result


print(action())

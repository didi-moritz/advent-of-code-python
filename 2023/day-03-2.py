import re

with open('day-03.data') as f:
    data = [line.rstrip('\n') for line in f]

width = len(data[0])
height = len(data)

digit_pattern = re.compile(r'\d')
number_pattern = re.compile(r'\d+')


def mark(x, y, found):
    found[y][x] = data[y][x]


def check_point(x, y, found):
    if x < 0 or x >= width or y < 0 or y >= height:
        return

    if digit_pattern.match(found[y][x]):
        return

    if digit_pattern.match(data[y][x]):
        mark(x, y, found)
        check_point(x - 1, y, found)
        check_point(x + 1, y, found)
        return True

    return False


def gear_power(symbol_x, symbol_y):
    found = [[' '] * width for y in range(height)]
    numbers_found = 0

    for y in range(symbol_y - 1, symbol_y + 2):
        for x in range(symbol_x - 1, symbol_x + 2):
            if check_point(x, y, found):
                numbers_found += 1

    if numbers_found == 2:
        power = 1
        for y in range(height):
            line = ''.join(found[y])
            for number in number_pattern.findall(line):
                power *= int(number)

        return power

    return 0


def action():
    result = 0
    for y in range(height):
        for x in range(width):
            if data[y][x] == '*':
                result += gear_power(x, y)

    return result


print(action())

import re

with open('day-03.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile("^\s*(\d+)\s+(\d+)\s+(\d+)$")


def read_number(x, y):
    return int(line_pattern.match(data[y]).groups()[x])


def action():
    correct_count = 0
    for y in range(0, len(data), 3):
        for x in range(3):
            numbers = [read_number(x, y), read_number(x, y + 1), read_number(x, y + 2)]
            numbers.sort()
            if numbers[0] + numbers[1] > numbers[2]:
                correct_count += 1
                print(numbers)

    return correct_count


print(action())

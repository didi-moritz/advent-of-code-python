import re

with open('day-09.data') as f:
    data = [line.rstrip('\n') for line in f]

number_pattern = re.compile(r'-?\d+')


def next_numbers(numbers):
    diff: list[int] = []
    for i in range(0, len(numbers) - 1):
        diff.append(numbers[i + 1] - numbers[i])

    return diff


def check_finished(numbers):
    check = numbers[0]
    for i in range(1, len(numbers)):
        if check != numbers[i]:
            return False

    return True


def action():
    result = 0
    for line in data:
        numbers = list(map(int, number_pattern.findall(line)))
        numbers.reverse()
        
        nexts = [numbers]

        while not check_finished(nexts[-1]):
            nexts.append(next_numbers(nexts[-1]))

        for i in range(2, len(nexts) + 1):
            nexts[-i].append(nexts[-i][-1] + nexts[-i + 1][-1])

        result += nexts[0][-1]

    return result


print(action())

# 2416390430 too high

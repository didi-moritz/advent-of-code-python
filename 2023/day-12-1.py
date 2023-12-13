import re

with open('day-12.data') as f:
    data = [line.rstrip('\n') for line in f]

patterns = {}

line_pattern = re.compile(r'^([^ ]+) (.*)$')
any_pattern = re.compile(r'.*#')


def get_pattern(num) -> re.Pattern:
    global patterns

    if num not in patterns:
        # patterns[num] = re.compile(rf'(\?|\.|^)[#?]{{{num}}}(\?|\.|$)')
        patterns[num] = re.compile(rf'[#?]{{{num}}}(\?|\.|$)')
        # patterns[num] = re.compile(rf'[^#]??[#?]{{{num}}}[^#]')

    return patterns[num]


def find_arrangements(springs, numbers, pos=0):
    if len(numbers) == 0:
        if not any_pattern.match(springs, pos):
            return 1
        else:
            return 0

    new_numbers = numbers.copy()
    number = new_numbers.pop(0)
    pattern = get_pattern(number)

    result = 0
    for i in range(pos, len(springs)):
        if i == pos or springs[i - 1] != '#':
            match = pattern.match(springs, i)
            if match:
                result += find_arrangements(springs, new_numbers, i + number + 1)

        if springs[i] == '#':
            break

    return result


def action():
    result = 0
    for line in data:
        springs, numbers_text = line_pattern.match(line).groups()
        numbers = list(map(int, numbers_text.split(',')))

        result += find_arrangements(springs, numbers)

    return result


print(action())

# 10296 too high

# 8660 too high

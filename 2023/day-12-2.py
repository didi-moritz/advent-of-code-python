import re
import time

with open('day-12.data') as f:
    data = [line.rstrip('\n') for line in f]

patterns = {}

line_pattern = re.compile(r'^([^ ]+) (.*)$')
any_pattern = re.compile(r'#')


def get_pattern(num) -> re.Pattern:
    global patterns

    if num not in patterns:
        patterns[num] = re.compile(rf'[^#]*?([^.]{{{num}}})(\?|\.|$)')

    return patterns[num]


def get_cache_key(level, pos):
    return f'{level};{pos}'


def find_arrangements(cache, springs, numbers, level=0, pos=0):
    cache_key = get_cache_key(level, pos)

    if cache_key in cache:
        return cache[cache_key]

    if level == len(numbers):
        return 0 if any_pattern.search(springs, pos) else 1

    number = numbers[level]
    pattern = get_pattern(number)

    result = 0
    i = pos
    while True:
        match = pattern.match(springs, i)
        if not match:
            break

        i = match.regs[1][0]

        result += find_arrangements(cache, springs, numbers, level + 1, i + number + 1)

        if springs[i] == '#':
            break

        i += 1

    cache[cache_key] = result
    return result


def action():
    result = 0
    for i in range(len(data)):
        start = time.time()
        line = data[i]
        springs, numbers_text = line_pattern.match(line).groups()
        springs = '?'.join([springs] * 5)
        numbers = list(map(int, numbers_text.split(',')))
        numbers = numbers * 5

        arrangements = find_arrangements({}, springs, numbers)
        result += arrangements

        end = time.time()
        print(i, 'of', len(data), arrangements, f'{end - start}s')

    return result


start_run = time.time()
print(action())
end_run = time.time()

print(f'{end_run - start_run}s')

import math
import re
from functools import reduce

with open('day-04.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile("^(.+)-(\d+)\[(.*)\]$")


def check(letters, checksum):
    letter_map = {}
    for letter in letters:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    ordered_letters = dict(
        sorted(letter_map.items(), key=lambda item: f'{(len(letters) - item[1]) / 1000}-{item[0]}')).keys()

    check_checksum = reduce(lambda a, b: f'{a}{b}', ordered_letters)[:5]

    return checksum == check_checksum


def action():
    result = 0;
    for line in data:
        text, sector_id, checksum = line_pattern.match(line).groups()
        letters = list(text.replace('-', ''))

        if check(letters, checksum):
            result += int(sector_id)

    return result


print(action())

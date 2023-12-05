import re

with open('day-01.data') as f:
    data = [line.rstrip('\n') for line in f]

first_digit_pattern = re.compile(r'^\D*(\d)')
last_digit_pattern = re.compile(r'(\d)\D*$')


def action():
    result = 0
    for line in data:
        first_digit = int(first_digit_pattern.match(line).group(1))
        last_digit = int(last_digit_pattern.search(line).group(1))

        number = first_digit * 10 + last_digit
        result += number

    return result


print(action())

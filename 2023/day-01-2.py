import re

with open('day-01.data') as f:
    data = [line.rstrip('\n') for line in f]

first_word_pattern = re.compile(r'^\D*?(one|two|three|four|five|six|seven|eight|nine|\d)')
last_word_pattern = re.compile(r'.*(one|two|three|four|five|six|seven|eight|nine|\d)\D*?$')

number_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def parse_word(word):
    if word in number_dict:
        return number_dict[word]

    return int(word)


def action():
    result = 0
    for line in data:
        first_word = first_word_pattern.match(line).group(1)
        last_word = last_word_pattern.match(line).group(1)

        number = parse_word(first_word) * 10 + parse_word(last_word)
        result += number

    return result


print(action())

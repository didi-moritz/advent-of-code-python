import re
from functools import reduce

with open('day-04.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile(r'^(.+)-(\d+)\[(.*)]$')


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


def rotate_letter(letter, steps):
    if letter == '-':
        return ' '

    return chr(((ord(letter) - ord('a') + steps) % (ord('z') - ord('a') + 1)) + ord('a'))


def rotate_text(text, steps):
    return reduce(lambda a, b: f'{a}{b}', list(map(lambda letter: rotate_letter(letter, steps), text)))


def action():
    result = ''
    for line in data:
        text, sector_id, checksum = line_pattern.match(line).groups()
        letters = list(text.replace('-', ''))

        if check(letters, checksum):
            decrypted_text = rotate_text(text, int(sector_id))
            output = f'{decrypted_text} -> {sector_id}'
            print(output)

            if decrypted_text == 'northpole object storage':
                result = output

    return result


print(action())

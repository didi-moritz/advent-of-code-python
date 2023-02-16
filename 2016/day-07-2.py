import re
from functools import reduce

with open('day-07.data') as f:
    data = [line.rstrip('\n') for line in f]

sequences_pattern = re.compile(r'(^|])([^[]+)')
hypernet_sequences_pattern = re.compile(r'\[([^]]+)]')
aba_pattern = re.compile(r'(.)(.)\1')

result = 0


def get_abas(text):
    return list(filter(lambda i: i[0] != i[1],
                       aba_pattern.findall(text) + aba_pattern.findall(reversed_text(text))))


def reversed_text(text):
    return reduce(lambda a, b: f'{b}{a}', text)


for line in data:
    parts = list(map(lambda i: i[1], sequences_pattern.findall(line)))
    hypernet = reduce(lambda a, b: f'{a} {b}', hypernet_sequences_pattern.findall(line))

    found = False

    for part in parts:
        abas = get_abas(part)
        for aba in abas:
            bab = f'{aba[1]}{aba[0]}{aba[1]}'
            if bab in hypernet:
                found = True

    if found:
        print(line)
        result += 1

print(result)

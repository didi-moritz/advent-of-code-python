import re

with open('day-07.data') as f:
    data = [line.rstrip('\n') for line in f]

sequences_pattern = re.compile(r'(^|])([^[]+)')
hypernet_sequences_pattern = re.compile(r'\[([^]]+)]')
abba_pattern = re.compile(r'(.)(.)\2\1')

result = 0


def is_abba(text):
    matches = list(filter(lambda i: i[0] != i[1], abba_pattern.findall(text)))
    return len(matches) > 0


for line in data:
    parts = list(map(lambda i: i[1], sequences_pattern.findall(line)))

    found = False

    for part in parts:
        found = found or is_abba(part)

    if found:
        hypernet_parts = hypernet_sequences_pattern.findall(line)
        for part in hypernet_parts:
            found = found and not is_abba(part)

    if found:
        result += 1

print(result)

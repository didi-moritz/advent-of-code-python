import re

with open('day-16.data') as f:
    data = [line.rstrip('\n') for line in f]

conditions = ['children: 3',
              'samoyeds: 2',
              'akitas: 0',
              'vizslas: 0',
              'cars: 2',
              'perfumes: 1']


def to_list_with_pattern(d: dict):
    return list(map(lambda k: {'value': d[k], 'pattern': re.compile(f'.*{k}: (\d+).*')}, d))


greater_conditions = to_list_with_pattern({'cats': 7, 'trees': 3})
fewer_conditions = to_list_with_pattern({'pomeranians': 3, 'goldfish': 5})

print(greater_conditions)

for line in data:
    check = True
    for condition in conditions:
        if condition not in line:
            if condition.split(':')[0] in line:
                check = False
                break

    if not check:
        continue

    for condition in greater_conditions:
        match = condition['pattern'].match(line)
        if match and int(match.groups()[0]) <= condition['value']:
            check = False
            break

    if not check:
        continue

    for condition in fewer_conditions:
        match = condition['pattern'].match(line)
        if match and int(match.groups()[0]) >= condition['value']:
            check = False
            break

    if check:
        print(line)

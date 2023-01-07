with open('day-16.data') as f:
    data = [line.rstrip('\n') for line in f]

conditions = ['children: 3',
              'cats: 7',
              'samoyeds: 2',
              'pomeranians: 3',
              'akitas: 0',
              'vizslas: 0',
              'goldfish: 5',
              'trees: 3',
              'cars: 2',
              'perfumes: 1']

for line in data:
    check = True
    for condition in conditions:
        if condition not in line:
            if condition.split(':')[0] in line:
                check = False
                break

    if check:
        print(line)

with open('day-04.data') as f:
    data = [line.rstrip('\n') for line in f]

score = 0
for line in data:
    range1, range2 = line.split(',')
    range1_from, range1_to = [int(i) for i in range1.split('-')]
    range2_from, range2_to = [int(i) for i in range2.split('-')]
    if ((range1_from <= range2_from and range1_to >= range2_to)
            or (range2_from <= range1_from and range2_to >= range1_to)):
        score += 1
        print(f'{line} {score}')

print(score)

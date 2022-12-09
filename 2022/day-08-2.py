with open('day-08.data') as f:
    data = [line.rstrip('\n') for line in f]

trees = []

for y in range(0, len(data)):
    trees.append([])
    for x in range(0, len(data[y])):
        trees[y].append(int(data[y][x]))

score = 0


def calc_score():
    number = trees[y][x]
    total = 1
    count = 1
    for i in range(x + 1, len(trees[y]) - 1):
        if trees[y][i] >= number:
            break
        count += 1
    total *= count

    count = 1
    for i in range(x - 1, 0, -1):
        if trees[y][i] >= number:
            break
        count += 1
    total *= count

    count = 1
    for i in range(y + 1, len(trees) - 1):
        if trees[i][x] >= number:
            break
        count += 1
    total *= count

    count = 1
    for i in range(y - 1, 0, -1):
        if trees[i][x] >= number:
            break
        count += 1
    total *= count

    return total


for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[y]) - 1):
        score = max(score, calc_score())

print(score)

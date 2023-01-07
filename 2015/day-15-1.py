import re

with open('day-15.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile('^.* (-?\d+), .* (-?\d+), .* (-?\d+), .* (-?\d+), .*$')

ingredients = []


def load():
    for line in data:
        ingredients.append([int(n) for n in line_pattern.match(line).groups()])


load()

attributes_count = len(ingredients[0])

MAX_AMOUNTS = 100

max_score = 0


def action(amounts):
    global max_score

    total_amounts = 0
    for amount in amounts:
        total_amounts += amount

    if total_amounts >= MAX_AMOUNTS:
        return

    if len(amounts) == len(ingredients) - 1:
        amounts.append(MAX_AMOUNTS - total_amounts)

        score = 1
        for i in range(attributes_count):
            attributes_score = 0
            for j in range(len(amounts)):
                attributes_score += amounts[j] * ingredients[j][i]
            score *= max(0, attributes_score)

        max_score = max(max_score, score)
        return

    for i in range(MAX_AMOUNTS - total_amounts + 1):
        new_amounts = amounts.copy()
        new_amounts.append(i)
        action(new_amounts)


action([])

print(max_score)

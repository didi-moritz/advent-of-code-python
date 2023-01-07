import re

with open('day-15.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile('^.* (-?\d+), .* (-?\d+), .* (-?\d+), .* (-?\d+), .*(\d+)$')

ingredients = []


def load():
    for line in data:
        ingredients.append([int(n) for n in line_pattern.match(line).groups()])


load()

attributes_count = len(ingredients[0]) - 1

MAX_AMOUNTS = 100

TARGET_CALORIES = 500

max_score = 0


def action(amounts, calories):
    global max_score

    total_amounts = 0
    for amount in amounts:
        total_amounts += amount

    if total_amounts >= MAX_AMOUNTS:
        return

    remaining_amounts = MAX_AMOUNTS - total_amounts
    if len(amounts) == len(ingredients) - 1:
        if calories + remaining_amounts * ingredients[-1][-1] != TARGET_CALORIES:
            return

        amounts.append(remaining_amounts)

        score = 1
        for i in range(attributes_count):
            attributes_score = 0
            for j in range(len(amounts)):
                attributes_score += amounts[j] * ingredients[j][i]
            score *= max(0, attributes_score)

        max_score = max(max_score, score)
        return

    for i in range(remaining_amounts + 1):
        new_calories = calories + ingredients[len(amounts)][attributes_count] * i
        if new_calories <= TARGET_CALORIES:
            new_amounts = amounts.copy()
            new_amounts.append(i)
            action(new_amounts, new_calories)


action([], 0)

print(max_score)

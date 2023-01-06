import re

with open('day-13.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile('^([^ ]+) .*(gain|lose) (\d+) .* ([^ ]+).$')

happiness = {}

for line in data:
    p1, gain_lose, points, p2 = line_pattern.match(line).groups()
    if p1 not in happiness:
        happiness[p1] = {}
    happiness[p1][p2] = int(points) * (-1 if gain_lose == 'lose' else 1)

people = list(happiness.keys())

max_happiness = 0


def action(p, already_positioned, score):
    global max_happiness

    if len(already_positioned) == len(people) - 1:
        max_happiness = max(max_happiness,
                            score
                            + happiness[p][already_positioned[0]]
                            + happiness[already_positioned[0]][p])
        return

    new_already_positioned = already_positioned.copy()
    new_already_positioned.append(p)

    for new_p in people:
        if new_p not in new_already_positioned:
            action(new_p, new_already_positioned,
                   score
                   + happiness[p][new_p]
                   + happiness[new_p][p])


action(people[0], [], 0)

print(max_happiness)

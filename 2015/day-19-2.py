import random

with open('day-19.data') as f:
    data = [line.rstrip('\n') for line in f]

rules = []
MAX_INT = 100000


def load():
    for i in range(len(data) - 2):
        rules.append(tuple(data[i].split(' => ')))


load()

FINAL_WORD = 'e'


def action():
    word = data[-1]

    steps = 0

    while True:
        changed = False
        if word == FINAL_WORD:
            return steps

        for rule in rules:
            pos = 0
            while True:
                pos = word.find(rule[1], pos)
                if pos >= 0:
                    word = word[:pos] + rule[0] + word[pos + len(rule[1]):]
                    steps += 1
                    changed = True
                else:
                    break

        if not changed:
            return -1


while True:
    random.shuffle(rules)
    result = action()
    if result > 0:
        print(result)
        break

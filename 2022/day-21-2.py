import copy
import math
import re

with open('day-21.data') as f:
    data = [line.rstrip('\n') for line in f]


class Monkey:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def is_solved(self):
        return self.number is not None

    def is_solvable(self):
        return False


class NumberMonkey(Monkey):

    def __init__(self, name, number):
        Monkey.__init__(self, name, number)


class OperatorMonkey(Monkey):

    def __init__(self, name, var_1, var_2, operator):
        Monkey.__init__(self, name, None)
        self.var_1 = var_1
        self.var_2 = var_2
        self.value_1 = None
        self.value_2 = None
        self.operator = operator

    def is_solvable(self):
        return not self.is_solved() and self.value_1 is not None and self.value_2 is not None

    def __str__(self):
        return f'{self.name}: {self.value_1 or self.var_1} {self.operator} {self.value_2 or self.var_2}'


number_pattern = re.compile('^(.+): (\d+)$')
operator_pattern = re.compile('^(.+): (.+) (.) (.+)$')

monkeys = {}

for line in data:
    number_pattern_match = number_pattern.match(line)
    if number_pattern_match:
        name, number = number_pattern_match.groups()
        monkeys[name] = NumberMonkey(name, number)
    else:
        name, var_1, operator, var_2 = operator_pattern.match(line).groups()
        monkeys[name] = OperatorMonkey(name, var_1, var_2, operator)

root = monkeys['root']
humn = monkeys['humn']

del monkeys['root']
del monkeys['humn']

while True:
    action = False
    for monkey in monkeys.values():

        if monkey.is_solved():
            continue

        if monkey.value_1 is None and monkey.var_1 not in [humn.name, root.name] and monkeys[monkey.var_1].is_solved():
            monkey.value_1 = monkeys[monkey.var_1].number

        if monkey.value_2 is None and monkey.var_2 not in [humn.name, root.name] and monkeys[monkey.var_2].is_solved():
            monkey.value_2 = monkeys[monkey.var_2].number

        if monkey.is_solvable():
            monkey.number = int(eval(
                f'{monkey.value_1} {monkey.operator} {monkey.value_2}'))
            action = True

    if not action:
        break

important_monkeys = dict(
    filter(lambda item: not item[1].is_solved() or item[0] in [root.var_1, root.var_2], monkeys.items()))

humn_number = 0
last_diff = None
steps = 1000000000000

while True:
    monkeys = copy.deepcopy(important_monkeys)

    while True:
        for monkey in monkeys.values():
            if monkey.is_solved():
                continue

            if monkey.value_1 is None:
                if monkey.var_1 == 'humn':
                    monkey.value_1 = humn_number
                elif monkeys[monkey.var_1].is_solved():
                    monkey.value_1 = monkeys[monkey.var_1].number

            if monkey.value_2 is None:
                if monkey.var_2 == 'humn':
                    monkey.value_2 = humn_number
                elif monkeys[monkey.var_2].is_solved():
                    monkey.value_2 = monkeys[monkey.var_2].number

            if monkey.is_solvable():
                monkey.number = eval(
                    f'{monkey.value_1} {monkey.operator} {monkey.value_2}')

        if monkeys[root.var_1].is_solved() and monkeys[root.var_2].is_solved:
            break

    value_1 = int(monkeys[root.var_1].number)
    value_2 = int(monkeys[root.var_2].number)

    if value_1 == value_2:
        print(humn_number)
        break

    diff = value_1 - value_2

    if last_diff is not None:
        if math.copysign(1, diff) != math.copysign(1, last_diff) or abs(diff) > abs(last_diff):
            steps = int(steps * -0.5)

    last_diff = diff
    humn_number += steps

    print(
        f'{humn_number} - {monkeys[root.var_1].number} vs. {monkeys[root.var_2].number} -> {abs(monkeys[root.var_1].number - monkeys[root.var_2].number)} - {steps}')

    humn_number += 1

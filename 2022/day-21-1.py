import re

with open('day-21.data') as f:
    data = [line.rstrip('\n') for line in f]


class Monkey:

    def __init__(self, name: str, number: int, solved: bool):
        self.name = name
        self.number = number
        self.solved = solved


class NumberMonkey(Monkey):

    def __init__(self, name, number):
        Monkey.__init__(self, name, number, True)


class OperatorMonkey(Monkey):

    def __init__(self, name, var_1, var_2, operator):
        Monkey.__init__(self, name, None, False)
        self.var_1 = var_1
        self.var_2 = var_2
        self.operator = operator


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

while not monkeys['root'].solved:
    for monkey in monkeys.values():
        if monkey.solved:
            continue

        if monkeys[monkey.var_1].solved and monkeys[monkey.var_2].solved:
            monkey.number = int(eval(
                f'{monkeys[monkey.var_1].number} {monkey.operator} {monkeys[monkey.var_2].number}'))
            monkey.solved = True

print(monkeys['root'].number)

import re

with open('day-11.data') as f:
    data = [line.rstrip('\n') for line in f]


class Monkey:
    def __init__(self, operation_string):
        self.items = []
        self.operation = lambda old: eval(operation_string)
        self.test_number = 0
        self.match = 0
        self.non_match = 0
        self.inspection_count = 0


items_pattern = re.compile('.* items: (.*)$')
operation_pattern = re.compile('.* new = (.*)$')
test_number_pattern = re.compile('.* divisible by (.*)$')
match_pattern = re.compile('.* throw to monkey (.*)$')

monkeys = []

for i in range(1, len(data), 7):
    monkey = Monkey(operation_pattern.match(data[i + 1]).group(1))
    monkey.items = eval('[' + items_pattern.match(data[i]).group(1) + ']')
    monkey.test_number = int(test_number_pattern.match(data[i + 2]).group(1))
    monkey.match = int(match_pattern.match(data[i + 3]).group(1))
    monkey.non_match = int(match_pattern.match(data[i + 4]).group(1))
    monkeys.append(monkey)

for i in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            item = monkey.operation(item)
            item = int(item / 3)
            to_monkey = monkey.match if item % monkey.test_number == 0 else monkey.non_match
            monkeys[to_monkey].items.append(item)
            monkey.inspection_count += 1
        monkey.items = []

monkeys.sort(key=lambda monkey: monkey.inspection_count, reverse=True)

print(monkeys[0].inspection_count * monkeys[1].inspection_count)

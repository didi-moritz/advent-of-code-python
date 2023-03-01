import re
from enum import Enum

with open('day-10.data') as f:
    data = [line.rstrip('\n') for line in f]

value_to_bot_pattern = re.compile(r'^value (\d+) goes to bot (\d+)$')
bot_pattern = re.compile(r'^bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)$')

bots = [[] for i in range(1000)]


class Rule:
    def __init__(self, low_type, low_number, high_type, high_number):
        self.low_type = low_type
        self.low_number = low_number
        self.high_type = high_type
        self.high_number = high_number


rules = {}


def load():
    for line in data:
        if value_to_bot_pattern.match(line):
            value, bot = list(map(int, value_to_bot_pattern.match(line).groups()))
            bots[bot].append(value)
        else:
            bot, low_type, low_number, high_type, high_number = bot_pattern.match(line).groups()
            rules[int(bot)] = Rule(low_type, int(low_number), high_type, int(high_number))


load()


def action():
    while True:
        bot = None
        for i in range(len(bots)):
            if len(bots[i]) == 2:
                bot = i
                break
                
        low_value = min(bots[bot])
        high_value = max(bots[bot])

        if low_value == 17 and high_value == 61:
            print(bot)
            exit(0)

        bots[bot] = []
        rule = rules[bot]
        if rule.low_type == 'bot':
            bots[rule.low_number].append(low_value)
        if rule.high_type == 'bot':
            bots[rule.high_number].append(high_value)


action()

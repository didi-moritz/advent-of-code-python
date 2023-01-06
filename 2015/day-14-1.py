import re

with open('day-14.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile('^.* (\d+) .* (\d+) .* (\d+) .*$')


class Reindeer:

    def __init__(self, params):
        self.kms = params[0]
        self.fly_seconds = params[1]
        self.rest_seconds = params[2]


reindeers: list[Reindeer] = []


def load():
    for line in data:
        reindeers.append(Reindeer(tuple(int(n) for n in line_pattern.match(line).groups())))


load()

minutes = 2503

max_kms = 0

for reindeer in reindeers:
    full_cycle_seconds = reindeer.fly_seconds + reindeer.rest_seconds
    full_cycles = int(minutes / full_cycle_seconds)

    rest_fly_seconds = min(reindeer.fly_seconds, minutes - full_cycles * full_cycle_seconds)

    kms = (full_cycles * reindeer.fly_seconds + rest_fly_seconds) * reindeer.kms
    print(kms)

    max_kms = max(max_kms, kms)

print(max_kms)

# 1120 too_low

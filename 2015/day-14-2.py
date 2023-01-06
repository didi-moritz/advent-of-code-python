import re

with open('day-14.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile('^.* (\d+) .* (\d+) .* (\d+) .*$')


class Reindeer:

    def __init__(self, params):
        self.kms = params[0]
        self.fly_seconds = params[1]
        self.rest_seconds = params[2]
        self.points = 0

    def get_kms(self, minute):
        full_cycle_seconds = self.fly_seconds + self.rest_seconds
        full_cycles = int(minute / full_cycle_seconds)

        rest_fly_seconds = min(self.fly_seconds, minute - full_cycles * full_cycle_seconds)

        return (full_cycles * self.fly_seconds + rest_fly_seconds) * self.kms

    def add_point(self):
        self.points += 1


reindeers: list[Reindeer] = []


def load():
    for line in data:
        reindeers.append(Reindeer(tuple(int(n) for n in line_pattern.match(line).groups())))


load()

minutes = 2503


def action():
    for minute in range(1, minutes + 1):
        forwardest_reindeers = []
        best_kms = 0
        for reindeer in reindeers:
            kms = reindeer.get_kms(minute)
            if kms > best_kms:
                forwardest_reindeers = []
                best_kms = kms

            if kms == best_kms:
                forwardest_reindeers.append(reindeer)

        for reindeer in forwardest_reindeers:
            reindeer.add_point()


action()

max_points = 0

for reindeer in reindeers:
    max_points = max(max_points, reindeer.points)

print(max_points)

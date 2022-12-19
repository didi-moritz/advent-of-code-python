import re
import sys
from itertools import chain, combinations

sys.setrecursionlimit(10000)

with open('day-16.data') as f:
    data = [line.rstrip('\n') for line in f]

valves = {}


class Valve:
    def __init__(self, name: str, rate: int):
        self.name = name
        self.rate = rate
        self.to_valves = []
        self.from_valves = []

    def set_to_valves(self, to_valves):
        self.to_valves = to_valves

    def add_from_valve(self, from_valve):
        self.from_valves.append(from_valve)


def read_valves():
    line_pattern = re.compile('Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)$')
    for line in data:
        a, b, _c = line_pattern.match(line).groups()
        valves[a] = Valve(a, int(b))
    for line in data:
        a, _b, c = line_pattern.match(line).groups()
        to_valves = [valves[name] for name in c.split(', ')]
        valve = valves[a]
        valve.set_to_valves(to_valves)
        for to_valve in to_valves:
            to_valve.add_from_valve(valve)


read_valves()

openable_valves = list(filter(lambda v: v.rate > 0, valves.values()))

steps_needed = {}


def build_info():
    for to_valve in openable_valves:
        for from_valve in openable_valves + [valves['AA']]:
            steps_needed[from_valve.name + to_valve.name] = find_parent(to_valve, from_valve, [], 0)


def find_parent(valve, parent, already_visited, steps):
    if valve == parent:
        return steps

    if valve in already_visited or steps > 29:
        return 1000

    min_steps = 1000
    for from_valve in valve.from_valves:
        min_steps = min(min_steps, find_parent(from_valve, parent, already_visited + [valve], steps + 1))

    return min_steps


build_info()

max_score = 0


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def do():
    global max_score

    for openable_valves_1 in list(powerset(openable_valves)):
        if len(openable_valves_1) > 0:
            openable_valves_2 = list(filter(lambda v: v not in openable_valves_1, openable_valves))
            max_score = max(
                max_score,
                action(valves['AA'], 26, list(openable_valves_1), 0) + action(valves['AA'], 26, openable_valves_2, 0))
            print(max_score)


def action(valve, minutes, remaining_openable_valves: list[Valve], score):
    best_score = score

    for to_valve in remaining_openable_valves:
        new_minutes = minutes - steps_needed[valve.name + to_valve.name] - 1
        if new_minutes > 0:
            new_score = score + (to_valve.rate * new_minutes)
            new_remaining_openable_valves = remaining_openable_valves.copy()
            new_remaining_openable_valves.remove(to_valve)
            best_score = max(
                best_score,
                action(to_valve, new_minutes, new_remaining_openable_valves, new_score))

    return best_score


do()

print('=' * 4)
print(max_score)

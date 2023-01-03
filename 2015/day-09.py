import copy
import re

with open('day-09.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile('^(.*) to (.*) = (\d+)$')

ways = {}
all_ways = []


def load():
    for line in data:
        location_from, location_to, distance = line_pattern.match(line).groups()
        if location_from not in ways:
            ways[location_from] = {}

        if location_to not in ways:
            ways[location_to] = {}

        ways[location_from][location_to] = int(distance)
        ways[location_to][location_from] = int(distance)

        all_ways.append((location_from, location_to, int(distance)))


load()

location_count = len(ways)

all_ways = sorted(all_ways, key=lambda item: item[2], reverse=False)

no_change = 0

min_steps = 1000000


def action(location_to, distance, already_visited):
    global min_steps

    if location_to in already_visited:
        return

    if distance > min_steps:
        return

    new_already_visited = copy.deepcopy(already_visited)
    new_already_visited.append(location_to)

    if len(new_already_visited) == location_count:
        min_steps = min(min_steps, distance)
        return

    for new_location_to in ways[location_to]:
        action(new_location_to, distance + ways[location_to][new_location_to], new_already_visited)


for location_to in ways:
    action(location_to, 0, [])

print(min_steps)

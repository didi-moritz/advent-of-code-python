import re
from enum import Enum
from time import time

with open('day-19.data') as f:
    data = [line.rstrip('\n') for line in f]

items_pattern = re.compile(
    'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')

minutes = 32

ends = 0

fingerprints = {}


class Type(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


iterations = 0


def process_minute(minute, resources, robots):
    global ends

    max_geode = 0

    fingerprint = f'{minute}-{",".join(map(str, resources.values()))}-{",".join(map(str, robots.values()))}'
    if fingerprint in fingerprints:
        return -1
    fingerprints[fingerprint] = True

    new_resources = {}
    for t in Type:
        new_resources[t] = resources[t] + robots[t]

    if minute + 1 == minutes:
        ends += 1
        return new_resources[Type.GEODE]

    can_buy_all = True

    for t in Type:
        has_resources = True
        for need_type in robot_needs[t].keys():
            if robot_needs[t][need_type] > resources[need_type]:
                has_resources = False

        if not has_resources:
            can_buy_all = False
            continue

        had_resources_last_minute_as_well = True
        for need_type in robot_needs[t].keys():
            if robot_needs[t][need_type] > resources[need_type] - robots[need_type]:
                had_resources_last_minute_as_well = False

        if has_resources and not had_resources_last_minute_as_well:
            new_new_resources = new_resources.copy()
            for need_type in robot_needs[t].keys():
                new_new_resources[need_type] -= robot_needs[t][need_type]

            new_robots = robots.copy()
            new_robots[t] += 1
            max_geode = max(max_geode,
                            process_minute(minute + 1, new_new_resources, new_robots))

    if not can_buy_all:
        max_geode = max(max_geode, process_minute(minute + 1, new_resources, robots))

    return max_geode


score = 1


def process_blueprint():
    global score
    global ends
    global fingerprints
    start = time()
    resources = {}
    robots = {}
    ends = 0
    fingerprints = {}
    for t in Type:
        resources[t] = 0
        robots[t] = 1 if t == Type.ORE else 0

    max_geode_possible = process_minute(0, resources, robots)
    print(f'{id}: {max_geode_possible}')
    print(f'{id}: took {time() - start}s')
    print(f'{id}: ends: {ends}')
    score *= max_geode_possible


for i in range(1, 3):
    line = data[i]
    robot_needs = {}
    id, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = \
        map(int, items_pattern.match(line).groups())

    print(line)

    robot_needs[Type.ORE] = {Type.ORE: ore_ore}
    robot_needs[Type.CLAY] = {Type.ORE: clay_ore}
    robot_needs[Type.OBSIDIAN] = {Type.ORE: obsidian_ore, Type.CLAY: obsidian_clay}
    robot_needs[Type.GEODE] = {Type.ORE: geode_ore, Type.OBSIDIAN: geode_obsidian}

    process_blueprint()

print(score)

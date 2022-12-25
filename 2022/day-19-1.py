import re
from enum import Enum
from time import time

with open('day-19.data') as f:
    data = [line.rstrip('\n') for line in f]

items_pattern = re.compile(
    'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')

minutes = 24


class Type(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


def process_minute(minute, resources, robots):
    max_geode = 0

    new_resources = {}
    for t in Type:
        new_resources[t] = resources[t] + robots[t]

    if minute + 1 == minutes:
        return new_resources[Type.GEODE]

    can_buy_geode_roboter = False
    for t in reversed(Type):
        has_resources = True
        for need_type in robot_needs[t].keys():
            if robot_needs[t][need_type] > resources[need_type]:
                has_resources = False

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

    max_geode = max(max_geode, process_minute(minute + 1, new_resources, robots))

    return max_geode


score = 0


def process_blueprint():
    global score
    start = time()
    resources = {}
    robots = {}
    for t in Type:
        resources[t] = 0
        robots[t] = 1 if t == Type.ORE else 0

    max_geode_possible = process_minute(0, resources, robots)
    print(f'{id}: {max_geode_possible}')
    print(f'{id}: took {time() - start}s')
    score += id * max_geode_possible


for line in data:
    robot_needs = {}
    id, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = \
        map(int, items_pattern.match(line).groups())

    robot_needs[Type.ORE] = {Type.ORE: ore_ore}
    robot_needs[Type.CLAY] = {Type.ORE: clay_ore}
    robot_needs[Type.OBSIDIAN] = {Type.ORE: obsidian_ore, Type.CLAY: obsidian_clay}
    robot_needs[Type.GEODE] = {Type.ORE: geode_ore, Type.OBSIDIAN: geode_obsidian}

    process_blueprint()

print(score)

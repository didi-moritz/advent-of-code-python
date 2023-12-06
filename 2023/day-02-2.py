import re

with open('day-02.data') as f:
    data = [line.rstrip('\n') for line in f]

cubes_pattern = re.compile(r' (\d+) (red|green|blue)')


def calc_power(cubes_matches):
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    for cubes in cubes_matches:
        number = int(cubes[0])
        color = cubes[1]
        if number > max_cubes[color]:
            max_cubes[color] = number

    return max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]


def action():
    result = 0
    for line in data:
        cubes_matches = cubes_pattern.findall(line)
        power = calc_power(cubes_matches)

        result += power

    return result


print(action())

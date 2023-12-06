import re

with open('day-02.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile(r'Game (\d+): (.*)')

max_cubes = {"red": 12, "green": 13, "blue": 14}


def valid_balls(number, color):
    return int(number) <= max_cubes[color]


def valid_game(game):
    for cubes in game.split(", "):
        number, color = cubes.split(" ")
        if not valid_balls(number, color):
            return False

    return True


def valid_games(games):
    for game in games.split("; "):
        if not valid_game(game):
            return False

    return True


def action():
    result = 0
    for line in data:
        game_number, games = line_pattern.match(line).groups()

        if valid_games(games):
            result += int(game_number)

    return result


print(action())

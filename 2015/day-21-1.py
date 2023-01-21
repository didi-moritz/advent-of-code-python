import re

with open('day-21.data') as f:
    data = [line.rstrip('\n') for line in f]

weapons_data = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

armor_data = """
Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

rings_data = """
Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

line_pattern = re.compile(".*\s+(\d+)\s+(\d+)\s+(\d+)$")

enemy_line_pattern = re.compile(".*\s+(\d+)$")


class Thing:

    def __init__(self, cost, damage, armor):
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Player:

    def __init__(self, points, damage, armor):
        self.points = points
        self.damage = damage
        self.armor = armor

    def with_things(self, things: [Thing]):
        damage = self.damage
        armor = self.armor
        for thing in things:
            damage += thing.damage
            armor += thing.armor

        return Player(self.points, damage, armor)

    def clone(self):
        return Player(self.points, self.damage, self.armor)

    def get_hit(self, damage):
        self.points -= max(1, damage - self.armor)

    def is_dead(self):
        return self.points <= 0


def parse_data(data_text):
    things = []
    split = data_text.split("\n")
    for i in range(2, len(split)):
        cost, damage, armor = map(int, line_pattern.match(split[i]).groups())
        things.append(Thing(cost, damage, armor))

    return things


def load():
    points, damage, armor = map(lambda l: int(enemy_line_pattern.match(l).groups()[0]), data)

    return list(map(parse_data, [weapons_data, armor_data, rings_data])) + [Player(points, damage, armor)]


weapons, armors, rings, enemy_start = load()

me_start = Player(100, 0, 0)


def simulate(me: Player, enemy: Player):
    while True:
        enemy.get_hit(me.damage)
        if enemy.is_dead():
            return True

        me.get_hit(enemy.damage)
        if me.is_dead():
            return False


def action():
    min_costs = -1
    for weapon in weapons:
        for armor_i in range(len(armors) + 1):
            for rings_i_1 in range(len(rings) + 1):
                for rings_i_2 in range(rings_i_1 + 1, len(rings) + 1):
                    things = [weapon]
                    if armor_i < len(armors):
                        things.append(armors[armor_i])
                    if rings_i_1 < len(rings):
                        things.append(rings[rings_i_1])
                    if rings_i_2 < len(rings):
                        things.append(rings[rings_i_2])

                    if simulate(me_start.with_things(things), enemy_start.clone()):
                        costs = 0
                        for thing in things:
                            costs += thing.cost

                        print(costs)
                        if min_costs < 0 or costs < min_costs:
                            min_costs = costs

    return min_costs


print(action())

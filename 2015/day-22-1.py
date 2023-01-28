import re

with open('day-22.data') as f:
    data = [line.rstrip('\n') for line in f]

enemy_line_pattern = re.compile(".*\s+(\d+)$")


class Spell:

    def __init__(self, name, mana, damage=0, heal=0, armor=0, mana_gain=0, duration=1, immediately=True):
        self.name = name
        self.mana = mana
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.mana_gain = mana_gain
        self.duration = duration
        self.immediately = immediately

    def decrease_duration(self):
        self.duration -= 1

    def can_use(self):
        return self.duration > 0

    def is_immediately(self):
        return self.immediately

    def clone(self):
        return Spell(self.name, self.mana, self.damage, self.heal, self.armor, self.mana_gain, self.duration,
                     self.immediately)

    def __str__(self):
        return f'{self.name} ->\tmana: {self.mana}, damage: {self.damage}, heal: {self.heal}, armor: {self.armor}, mana_gain: {self.mana_gain}, duration: {self.duration}'

    def __hash__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


spells = [Spell('Magic Missile', 53, damage=4),
          Spell('Drain', 73, damage=2, heal=2),
          Spell('Shield', 113, armor=7, duration=6, immediately=False),
          Spell('Poison', 173, damage=3, duration=6, immediately=False),
          Spell('Recharge', 229, mana_gain=101, duration=5, immediately=False)]


class Player:

    def __init__(self, points, damage=0, mana=0, armor=0):
        self.points = points
        self.damage = damage
        self.mana = mana
        self.armor = armor

    def clone(self):
        return Player(self.points, self.damage, self.mana, self.armor)

    def get_hit(self, damage):
        self.points -= max(1, damage - self.armor)

    def can_use_spell(self, spell: Spell):
        return self.mana >= spell.mana

    def use_spell(self, spell: Spell):
        self.mana += spell.mana_gain
        self.points += spell.heal
        # if spell.armor > 0:
        #     self.armor = spell.armor

    def activate_spell(self, spell):
        self.mana -= spell.mana

    def hit_with_spell(self, spell: Spell):
        self.points -= spell.damage

    def is_dead(self):
        return self.points <= 0


def load():
    points, damage = map(lambda l: int(enemy_line_pattern.match(l).groups()[0]), data)

    return Player(points, damage)


enemy_start = load()

me_start = Player(50, mana=500)


def simulate(me: Player, enemy: Player):
    while True:
        enemy.get_hit(me.damage)
        if enemy.is_dead():
            return True

        me.get_hit(enemy.damage)
        if me.is_dead():
            return False


min_used_mana = 10000000


def action(me: Player, enemy: Player, current_spells: [Spell], mana_used, level):
    global min_used_mana

    first_new_me = me.clone()
    first_new_enemy = enemy.clone()
    first_new_spells = list(map(lambda s: s.clone(), current_spells))

    # Player turn  - run effects
    for active_spell in first_new_spells:
        first_new_me.use_spell(active_spell)
        first_new_enemy.hit_with_spell(active_spell)
        active_spell.decrease_duration()
    first_new_spells = list(filter(lambda s: s.can_use(), first_new_spells))

    # check enemy
    if first_new_enemy.is_dead():
        print(mana_used)
        if mana_used < min_used_mana:
            min_used_mana = mana_used
        return

    if mana_used >= min_used_mana:
        return

    for spell in spells:
        if first_new_me.can_use_spell(spell) and spell not in first_new_spells:

            new_me = first_new_me.clone()
            new_enemy = first_new_enemy.clone()
            new_mana_used = mana_used
            new_spells = list(map(lambda s: s.clone(), first_new_spells))

            # Player turn - spell
            new_spell: Spell = spell.clone()
            new_mana_used += new_spell.mana
            new_me.activate_spell(new_spell)
            new_spells.append(new_spell)

            if new_mana_used >= min_used_mana:
                continue

            # Enemy turn - run effects
            for active_spell in new_spells:
                new_me.use_spell(active_spell)
                new_enemy.hit_with_spell(active_spell)
                active_spell.decrease_duration()
            new_spells = list(filter(lambda s: s.can_use(), new_spells))

            new_me.armor = 0
            for active_spell in new_spells:
                if active_spell.armor > 0:
                    new_me.armor = active_spell.armor

            # check enemy
            if new_enemy.is_dead():
                print(new_mana_used)
                if new_mana_used < min_used_mana:
                    min_used_mana = new_mana_used
                continue

            # Enemy turn - attack
            new_me.get_hit(new_enemy.damage)

            if new_me.is_dead():
                continue

            action(new_me, new_enemy, new_spells, new_mana_used, level + 1)


action(me_start, enemy_start, [], 0, 0)

print(min_used_mana)

# 212 too low
# 851 too low
# 1412 too high
# not 1359
# not 1004
# not 1233
# not 1266
# not 1306

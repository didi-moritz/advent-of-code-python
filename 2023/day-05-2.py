import re

with open('day-05.data') as f:
    data = [line.rstrip('\n') for line in f]

seeds_pattern = re.compile(r'^seeds: (.*)$')
numbers_pattern = re.compile(r'(\d+) (\d+)')
mapping_title_pattern = re.compile(r'^(\D+)-to-(\D+) map:$')
mapping_pattern = re.compile(r'^(\d+) (\d+) (\d+)$')


class FromTo:

    def __init__(self, source_from, dest_from, num):
        self.source_from = source_from
        self.dest_from = dest_from
        self.num = num

    def find_from(self, number):
        diff = number - self.dest_from

        if diff < 0 or diff >= self.num:
            return None

        return self.source_from + diff


class Mapping:

    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.from_tos: list[FromTo] = []
        self.visited: dict[int, bool] = {}

    def add_mapping(self, source_from, dest_from, num):
        self.from_tos.append(FromTo(source_from, dest_from, num))

    def find_from(self, number):
        for from_to in self.from_tos:
            source_from = from_to.find_from(number)
            if source_from is not None:
                return source_from

        return number


class SeedPair:

    def __init__(self, start, num):
        self.start = start
        self.num = num

    def exists(self, seed):
        return self.start <= seed < self.start + self.num


mappings: dict[str, Mapping] = {}


def find_seed(dest, number):
    if dest == 'seed':
        return number

    mapping = mappings[dest]
    return find_seed(mapping.source, mapping.find_from(number))


def action():
    current_mapping: Mapping = None
    seed_pairs: list[SeedPair] = []

    for line in data:
        if seeds_pattern.match(line):
            pairs = numbers_pattern.findall(seeds_pattern.match(line).groups()[0])
            for pair in pairs:
                seed_pairs.append(SeedPair(int(pair[0]), int(pair[1])))
        elif mapping_title_pattern.match(line):
            source, dest = mapping_title_pattern.match(line).groups()
            current_mapping = Mapping(source, dest)
            mappings[dest] = current_mapping
        elif mapping_pattern.match(line):
            dest_from, source_from, num = map(int, mapping_pattern.match(line).groups())
            current_mapping.add_mapping(source_from, dest_from, num)

    for i in range(1000000):
        location = i + 41000000
        seed = find_seed('location', location)
        for seed_pair in seed_pairs:
            if seed_pair.exists(seed):
                return location

    return -1


print(action())

# 41222968

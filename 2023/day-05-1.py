import math
import re

with open('day-05.data') as f:
    data = [line.rstrip('\n') for line in f]

seeds_pattern = re.compile(r'^seeds: (.*)$')
numbers_pattern = re.compile(r'\d+')
mapping_title_pattern = re.compile(r'^(\D+)-to-(\D+) map:$')
mapping_pattern = re.compile(r'^(\d+) (\d+) (\d+)$')


class FromTo:

    def __init__(self, source_from, dest_from, num):
        self.source_from = source_from
        self.dest_from = dest_from
        self.num = num

    def find_to(self, number):
        diff = number - self.source_from

        if diff < 0 or diff >= self.num:
            return None

        return self.dest_from + diff


class Mapping:

    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.from_tos: list[FromTo] = []

    def add_mapping(self, source_from, dest_from, num):
        self.from_tos.append(FromTo(source_from, dest_from, num))

    def find_to(self, number):
        for from_to in self.from_tos:
            to = from_to.find_to(number)
            if to is not None:
                return to

        return number


mappings: dict[str, Mapping] = {}


def find_location(source, number):
    if source == 'location':
        return number

    mapping = mappings[source]
    return find_location(mapping.dest, mapping.find_to(number))


def action():
    current_mapping: Mapping = None
    seeds = None
    result = None

    for line in data:
        if seeds_pattern.match(line):
            seeds = map(int, numbers_pattern.findall(seeds_pattern.match(line).groups()[0]))
        elif mapping_title_pattern.match(line):
            source, dest = mapping_title_pattern.match(line).groups()
            current_mapping = Mapping(source, dest)
            mappings[source] = current_mapping
        elif mapping_pattern.match(line):
            dest_from, source_from, num = map(int, mapping_pattern.match(line).groups())
            current_mapping.add_mapping(source_from, dest_from, num)

    for seed in seeds:
        location = find_location('seed', seed)
        if not result or location < result:
            result = location

    return result


print(action())

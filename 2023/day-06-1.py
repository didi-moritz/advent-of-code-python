import re

with open('day-06.data') as f:
    data = [line.rstrip('\n') for line in f]

numbers_pattern = re.compile(r'\d+')
time_pattern = re.compile(r'Time: (.*)')
distance_pattern = re.compile(r'Distance: (.*)')


def calc_winning_ways(time, distance):
    count = 0
    for i in range(1, time + 1):
        way = (time - i) * i
        if way > distance:
            count += 1
        elif way <= distance and count > 0:
            return count

    return count


def action():
    result = 1
    times = list(map(int, numbers_pattern.findall(time_pattern.match(data[0]).groups()[0])))
    distances = list(map(int, numbers_pattern.findall(distance_pattern.match(data[1]).groups()[0])))

    for i in range(len(times)):
        result *= calc_winning_ways(times[i], distances[i])

    return result


print(action())

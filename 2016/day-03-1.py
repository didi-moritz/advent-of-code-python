import re

with open('day-03.data') as f:
    data = [line.rstrip('\n') for line in f]

line_pattern = re.compile("^\s*(\d+)\s+(\d+)\s+(\d+)$")

correct_count = 0

for line in data:
    numbers = list(map(int, line_pattern.match(line).groups()))
    numbers.sort()
    if numbers[0] + numbers[1] > numbers[2]:
        correct_count += 1
        print(numbers)

print(correct_count)

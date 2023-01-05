import re

with open('day-12.data') as f:
    data = [line.rstrip('\n') for line in f]

number_pattern = re.compile('-?\d+')

score = 0
for number in number_pattern.findall(data[0]):
    score += int(number)

print(score)

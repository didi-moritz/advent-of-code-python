with open('day-01.data') as f:
    data = [int(line.rstrip('\n')) for line in f]

count = 0
previous = -1
for depth in data:
    if -1 < previous < depth:
        count += 1
    previous = depth

print(count)

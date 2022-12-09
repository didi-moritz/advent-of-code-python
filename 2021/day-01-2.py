with open('day-01.data') as f:
    data = [int(line.rstrip('\n')) for line in f]

count = 0

for i in range(3, len(data)):
    if data[i] > data[i - 3]:
        count += 1

print(count)

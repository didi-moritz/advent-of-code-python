with open('day-02.data') as f:
    data = [line.rstrip('\n') for line in f]

x = 0
y = 0
aim = 0

for line in data:
    command = line.split(' ')[0]
    steps = int(line.split(' ')[1])

    if command == 'forward':
        x += steps
        y += aim * steps
    elif command == 'down':
        aim += steps
    else:
        aim -= steps

print(x * y)

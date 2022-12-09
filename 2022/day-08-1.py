with open('day-08.data') as f:
    data = [line.rstrip('\n') for line in f]

visible = []

for y in range(0, len(data)):
    a = []
    for x in range(0, len(data[y])):
        a.append(False)
    visible.append(a)

for y in range(0, len(data)):
    line = data[y]
    current = -1
    for x in range(0, len(line)):
        visibility = int(line[x])
        visible[y][x] = visible[y][x] or (visibility > current)
        current = max(current, visibility)

    current = -1
    for x in range(len(line) - 1, -1, -1):
        visibility = int(line[x])
        visible[y][x] = visible[y][x] or (visibility > current)
        current = max(current, visibility)

for x in range(0, len(data[0])):
    current = -1
    for y in range(0, len(data)):
        visibility = int(data[y][x])
        visible[y][x] = visible[y][x] or (visibility > current)
        current = max(current, visibility)

    current = -1
    for y in range(len(data) - 1, -1, -1):
        visibility = int(data[y][x])
        visible[y][x] = visible[y][x] or (visibility > current)
        current = max(current, visibility)

visible_count = 0
for y in range(0, len(visible)):
    for x in range(0, len(visible[y])):
        visible_count += 1 if visible[y][x] else 0

print(visible_count)

with open('day-06.data') as f:
    data = [line.rstrip('\n') for line in f]

line = data[0]


def check_stack() -> bool:
    for i in range(0, 14):
        c = stack.pop()
        if c in stack:
            return False
    return True


for pos in range(14, len(line)):
    stack = [*line[pos - 14:pos]]
    if check_stack():
        break

print(pos)

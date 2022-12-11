with open('day-23.data') as f:
    data = [line.rstrip('\n') for line in f]

register = []
for i in range(8):
    register.append(0)


def register_index(name):
    return ord(name) - ord('a')


def register_value_or_value(value):
    if ord(value[0]) >= ord('a'):
        return register[register_index(value)]
    else:
        return int(value)


pos = 0
mul_count = 0
while pos < len(data):
    action, x, y = data[pos].split(' ')
    if action == 'jnz' and register_value_or_value(x) != 0:
        pos += register_value_or_value(y)
        continue
    elif action == 'set':
        register[register_index(x)] = register_value_or_value(y)
    elif action == 'sub':
        register[register_index(x)] -= register_value_or_value(y)
    elif action == 'mul':
        mul_count += 1
        register[register_index(x)] *= register_value_or_value(y)

    pos += 1

print(mul_count)

with open('day-09.data') as f:
    data = [line.rstrip('\n') for line in f]

result = 0
for line in data:
    print(line)
    o = ''
    pos = 0
    while True:
        s = line.find('(', pos)
        if s >= 0:
            e = line.find(')', s)
            if e > 0:
                o = f'{o}{line[pos:s]}'
                command = line[s + 1:e]
                length, times = list(map(int, command.split('x')))
                pos = e + length + 1
                for i in range(times):
                    o = f'{o}{line[e + 1:e + length + 1]}'
            else:
                break
        else:
            break

    if pos < len(line):
        o = f'{o}{line[pos:]}'

    print(f'{o} -> {len(o)}')
    result += len(o)

print(result)

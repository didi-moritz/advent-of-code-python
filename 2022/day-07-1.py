with open('day-07.data') as f:
    data = [line.rstrip('\n') for line in f]

root = {'sum': 0}
parent = root
current = root
dirs = []
for line in data:
    if line == '$ ls':
        continue
    elif line == '$ cd ..':
        current = current['parent']
    elif line.startswith('$ cd '):
        current = {'sum': 0, 'parent': current}
        dirs.append(current)
    elif not line.startswith('dir'):
        size = int(line.split(' ')[0])
        d = current
        while 'parent' in d.keys():
            d['sum'] += size
            d = d['parent']

sum = 0
for d in dirs:
    if d['sum'] <= 100000:
        sum += d['sum']

print(sum)

with open('day-07.data') as f:
    data = [line.rstrip('\n') for line in f]

root = {'sum': 0}
parent = root
current = root
dirs = [root]
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
        root['sum'] += size

total_size = 70000000
needed_size = 30000000
free_size = total_size - root['sum']
freed_size = needed_size - free_size

dirs.sort(key=lambda item: item['sum'])

for d in dirs:
    if d['sum'] >= freed_size:
        print(d['sum'])
        break

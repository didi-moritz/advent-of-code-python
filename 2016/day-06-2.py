with open('day-06.data') as f:
    data = [line.rstrip('\n') for line in f]

LENGTH = len(data[0])

letters_map = [[] for i in range(LENGTH)]

for line in data:
    for i in range(LENGTH):
        letters_map[i].append(line[i])

for letters in letters_map:
    print(min(set(letters), key=letters.count), end='')

print()

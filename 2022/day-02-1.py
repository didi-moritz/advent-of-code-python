with open('day-02.data') as f:
    data = [line.rstrip('\n') for line in f]

enemy_map = {'A': 1, 'B': 2, 'C': 3}
myself_map = {'X': 1, 'Y': 2, 'Z': 3}

winning_map = {1: 3, 2: 1, 3: 2}

score = 0

for line in data:
    enemy = enemy_map[line[0]]
    myself = myself_map[line[2]]
    points = myself + (3 if enemy == myself else (0 if winning_map[enemy] == myself else 6))
    score += points
    print(f'{line} -> {points}')

print(score)

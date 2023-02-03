import re

with open('day-25.data') as f:
    data = [line.rstrip('\n') for line in f]

number_pattern = re.compile(".* (\d+), .* (\d+).")
target_row, target_column = list(map(int, number_pattern.match(data[0]).groups()))

value = 20151125
row = 1
col = 1

while row != target_row or col != target_column:
    if row == 1:
        row = col + 1
        col = 0
    else:
        row -= 1

    col += 1

    value = (value * 252533) % 33554393

print(value)

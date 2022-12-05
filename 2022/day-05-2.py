import re

with open('day-05.data') as f:
    data = [line.rstrip('\n') for line in f]

stack_numbers_line = 0
while data[stack_numbers_line][1] != '1':
    stack_numbers_line += 1

stacks_count = int((len(data[stack_numbers_line]) + 2) / 4)

stacks = []
for i in range(0, stacks_count):
    stacks.append([])
    for j in range(stack_numbers_line, 0, -1):
        char = data[j - 1][i * 4 + 1]
        if char != ' ':
            stacks[i].append(char)

for i in range(stack_numbers_line + 2, len(data)):
    line = data[i]
    print(line)
    count, from_stack, to_stack = [int(i) for i in (re.search('move (\d+) from (\d) to (\d)', line).groups())]
    temp_stack = []
    for j in range(0, count):
        temp_stack.append(stacks[from_stack - 1].pop())
    for j in range(0, count):
        stacks[to_stack - 1].append(temp_stack.pop())

result = ''
for i in range(0, stacks_count):
    result += stacks[i][-1]

print(result)

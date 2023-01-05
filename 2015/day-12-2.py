import sys

sys.setrecursionlimit(10000)

with open('day-12.data') as f:
    data = [line.rstrip('\n') for line in f]

input = eval(data[0])

score = 0


def action(o):
    global score

    if type(o) is dict:
        for key in o:
            if o[key] == 'red':
                return
        for key in o:
            action(o[key])

    elif type(o) is list:
        for i in o:
            action(i)
    elif type(o) is int:
        score += o


action(input)

print(score)

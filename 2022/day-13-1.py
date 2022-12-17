with open('day-13.data') as f:
    data = [line.rstrip('\n') for line in f]


def compare(left, right) -> int:
    type_left = type(left)
    type_right = type(right)

    print(f'{left} -> {type_left}')
    print(f'{right} -> {type_right}')

    if type_left == int and type_right == int:
        if left == right:
            return 0
        else:
            return -1 if left < right else 1

    left_list = [left] if type_left == int else left
    right_list = [right] if type_right == int else right

    for j in range(max(len(left_list), len(right_list))):
        if j == len(left_list):
            return -1
        elif j == len(right_list):
            return 1

        result = compare(left_list[j], right_list[j])
        if result != 0:
            return result

    return 0


score = 0
for i in range(0, len(data), 3):
    r = compare(eval(data[i]), eval(data[i + 1]))
    if r == -1:
        score += int(i / 3) + 1
        print(f'score: {score}')
    print()

print()
print(score)

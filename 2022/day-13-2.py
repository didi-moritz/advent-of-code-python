import functools

with open('day-13.data') as f:
    data = [line.rstrip('\n') for line in f]

lists = []
for d in data:
    if len(d) > 0:
        lists.append(eval(d))

divider_1 = [[2]]
divider_2 = [[6]]
lists.append(divider_1)
lists.append(divider_2)


def compare(left, right) -> int:
    type_left = type(left)
    type_right = type(right)

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


lists = sorted(lists, key=functools.cmp_to_key(compare))

for l in lists:
    print(l)

print((lists.index(divider_1) + 1) * (lists.index(divider_2) + 1))

import os
from functools import reduce
from hashlib import md5

door_id = 'reyedfim'

empty = '*'

result = [empty] * 8
i = 0


def print_result():
    os.system('clear')
    print(reduce(lambda a, b: f'{a}{b}', result))


print_result()

while empty in result:
    text = f'{door_id}{i}'
    code = md5(text.encode()).hexdigest()
    if code.startswith('00000'):
        if code[5].isnumeric():
            pos = int(code[5])
            if 0 <= pos < 8:
                if result[pos] == empty:
                    result[pos] = code[6]
                    print_result()
    i += 1

import re
from enum import Enum

with open('day-23.data') as f:
    data = [line.rstrip('\n') for line in f]

enemy_line_pattern = re.compile(".*\s+(\d+)$")


class Command(Enum):
    JUMP = 'jmp'
    JUMP_IF_EVEN = 'jie'
    JUMP_IF_ONE = 'jio'
    TRIPLE = 'tpl'
    HALF = 'hlf'
    INCREMENT = 'inc'


class Register:

    def __init__(self, name, value):
        self.value = value
        self.name = name

    def execute(self, command: Command):
        if command == Command.HALF:
            self.value = int(self.value / 2)
        elif command == Command.TRIPLE:
            self.value *= 3
        elif command == Command.INCREMENT:
            self.value += 1

        if self.value < 0:
            self.value = 0

    def is_even(self):
        return self.value % 2 == 0

    def __str__(self):
        return self.name


class Instruction:

    def __init__(self, command: Command, register: Register = None, offset=0):
        self.command = command
        self.register = register
        self.offset = offset

    def execute_and_get_offset(self):
        if self.register:
            self.register.execute(self.command)

        if self.command == Command.JUMP or \
                self.command == Command.JUMP_IF_EVEN and self.register.is_even() or \
                self.command == Command.JUMP_IF_ONE and self.register.value == 1:
            return self.offset

        return 1

    def __str__(self):
        return f'{self.command}, register={self.register}, offset={self.offset}'


instructions: list[Instruction] = []

a = Register('a', 1)
b = Register('b', 0)


def load():
    for line in data:
        words = line.split()
        command = Command(words[0])
        if command in [Command.INCREMENT, Command.HALF, Command.TRIPLE]:
            r = a if words[1] == 'a' else b
            instructions.append(Instruction(command, register=r))
        elif command == Command.JUMP:
            offset = int(words[1])
            instructions.append(Instruction(command, offset=offset))
        else:
            r = a if words[1][0] == 'a' else b
            offset = int(words[2])
            instructions.append(Instruction(command, register=r, offset=offset))


load()


def action():
    i = 0
    while i < len(instructions):
        print(f'{i} -> {a.value}')
        print(instructions[i])
        i += instructions[i].execute_and_get_offset()


action()

print(b.value)

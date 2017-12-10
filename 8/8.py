from collections import deque


def parse_condition(cond, registers):
    i = cond.index(' ')
    inst_str = 'registers[\'%s\'] %s' % (cond[:i], cond[i + 1:])
    return eval(inst_str)


def process_instruction(inst, registers):
    if parse_condition(inst['cond'], registers):
        if inst['op'] == 'inc':
            registers[inst['reg']] += inst['val']
        else:
            # decrease
            registers[inst['reg']] -= inst['val']


if __name__ == '__main__':
    registers = {}
    instructions = deque()
    with open('input.txt') as f:
        for line in f:
            a = line.split()
            reg = a[0]
            registers[reg] = 0
            op = a[1]
            val = int(a[2])
            cond = a[4:]
            inst = {'reg': reg,
                    'op': op,
                    'val': val,
                    'cond': ' '.join(cond)}
            instructions.append(inst)
    highest_val = float('-inf')  # for p2
    while instructions:
        process_instruction(instructions.popleft(), registers)
        highest_val = max(highest_val, max(registers.values()))  # for p2
    print(max(registers.values()))  # p1
    print(highest_val)  # p2

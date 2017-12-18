import multiprocessing.pool
from collections import defaultdict


def run_program(prg_id, instructions, inqueue=None, outqueue=None):
    registers = defaultdict(int)
    registers['p'] = prg_id
    prev_sound = None
    i = count = 0

    def get_val(key_or_val):
        """ Instructions contain either a value or reference to a register
        to retrieve a value. Returns appropriate value given either a
        string value or register key.
        """
        try:
            return int(key_or_val)
        except ValueError:
            return registers[key_or_val]

    while 0 <= i < len(instructions) - 1:
        inst = instructions[i]
        op = inst[0]

        if op == 'snd':
            # play sound
            prev_sound = get_val(inst[1])
            if outqueue:
                # part 2
                outqueue.put(get_val(inst[1]))
            count += 1
        elif op == 'set':
            # set reg
            registers[inst[1]] = get_val(inst[2])
        elif op == 'add':
            # increase reg
            registers[inst[1]] += get_val(inst[2])
        elif op == 'mul':
            # multiply reg
            registers[inst[1]] *= get_val(inst[2])
        elif op == 'mod':
            # mod reg
            registers[inst[1]] %= get_val(inst[2])
        elif op == 'rcv':
            # recover
            if inqueue:
                # part 2
                registers[inst[1]] = inqueue.get()
            elif registers[inst[1]] != 0:
                # part 1
                return prev_sound
        elif op == 'jgz':
            # jump
            if get_val(inst[1]) > 0:
                i += get_val(inst[2])
                continue
        i += 1
    return count


def solve(instructions):
    # part 1
    print('(P1) Recovered Frequency: %s' % run_program(0, instructions))

    # part 2
    pool = multiprocessing.pool.ThreadPool(processes=2)
    q0 = multiprocessing.Queue()
    q1 = multiprocessing.Queue()

    process_0 = pool.apply_async(run_program, (0, instructions, q0, q1))
    process_1 = pool.apply_async(run_program, (1, instructions, q1, q0))

    process_0.get()
    print('(P2) Total values sent by program 1: %s' % process_1.get())


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = [l.split() for l in f.readlines()]
    solve(instructions)

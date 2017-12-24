import os


def run_program(instructions):
    registers = {chr(x): 0 for x in range(97, 105)}
    i = mul_count = 0

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

        if op == 'set':
            # set reg
            registers[inst[1]] = get_val(inst[2])
        elif op == 'sub':
            # increase reg
            registers[inst[1]] -= get_val(inst[2])
        elif op == 'mul':
            # multiply reg
            registers[inst[1]] *= get_val(inst[2])
            mul_count += 1
        elif op == 'jnz':
            # jump
            if get_val(inst[1]) != 0:
                i += get_val(inst[2])
                continue
        i += 1
    return mul_count


def part_2_assembly_original():
    a = 1
    b = 81
    c = b
    b *= 100
    b -= -100000
    c = b
    c -= -17000
    while True:
        f = 1
        d = 2
        e = 2
        while True:
            g = d
            while True:
                g *= e
                g -= b
                if g == 0:
                    f = 0
                e -= 1
                g = e
                g -= b
                if g == 0:
                    break
            d -= -1
            g = d
            g -= b
            if g == 0:
                break
        if f == 0:
            h -= -1
        g = b
        g -= c
        if g == 0:
            return
        else:
            b -= 17


def part_2_assembly_optimized():
    h = 0
    b = 81
    c = b
    b *= 100
    b += 100000
    c = b + 17000

    while True:
        f = 1
        d = 2
        e = 2
        #print(b, c, d, e, f, h)
        while True:  # prime check for b
            # original doesn't have modulo, uses two loops to test d*e==b
            # instead for values of e
            if b % d == 0:
                f = 0
            d += 1
            if d != b:
                continue
            if f == 0:  # not prime
                h += 1
            if b == c:
                return h
            b += 17
            break


def solve(instructions):
    print('(P1): %s' % run_program(instructions))
    print('(P2): %s' % part_2_assembly_optimized())


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base_dir, 'input.txt')) as f:
        instructions = [l.split() for l in f.readlines()]
    solve(instructions)

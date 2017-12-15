A_FACTOR = 16807
B_FACTOR = 48271
MOD = 2147483647


def generator(n, factor, multiple=None):
    """Next value = Least significant 16 bits of n * factor % MOD.
    If multiple set, only yields when next value is a multiple of multiple.

    Args:
        n (int): Previous value
        factor (int): Multiplier to generate next value
        multiple (int): Desired multiple for yield value. Defaults to None

    Yields:
        int: Next value
    """
    while True:
        n = n * factor % MOD
        if multiple:
            if n % multiple == 0:
                yield n & 0xffff
        else:
            yield n & 0xffff


if __name__ == '__main__':
    with open('input.txt') as f:
        a_start = int(f.readline().split()[-1])
        b_start = int(f.readline().split()[-1])
    # part 1
    gen_a = generator(a_start, A_FACTOR)
    gen_b = generator(b_start, B_FACTOR)
    print('(P1) Final count: %s' % sum(next(gen_a) == next(gen_b)
                                       for _ in range(40000000)))
    # part 2
    gen_a = generator(a_start, A_FACTOR, 4)
    gen_b = generator(b_start, B_FACTOR, 8)
    print('(P2) Final count: %s' % sum(next(gen_a) == next(gen_b)
                                       for _ in range(5000000)))

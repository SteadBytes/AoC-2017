from functools import reduce


def basic_knot(lengths, rounds=1):
    l = [x for x in range(256)]
    # l = [0, 1, 2, 3, 4] # example
    i = skip = 0
    for _ in range(rounds):
        for x in lengths:
            # reverse order of x elements in list starting at i
            tmp = l[i:i + x]
            if i + x > len(l):
                ind = (i + x) - len(l)
                tmp += l[:ind]
            tmp = tmp[::-1]
            for j in range(len(tmp)):
                l[(i + j) % len(l)] = tmp[j]
            # increase i by x+skip
            i += x + skip
            i = i % len(l)
            skip += 1
    return l


def dense_hash(l):
    res = []
    for i in range(0, len(l), 16):
        res.append(reduce(lambda a, b: a ^ b, l[i:i + 16]))
    return res


def string_knot_hash(s):
    ascii_codes = [ord(x) for x in s] + [17, 31, 73, 47, 23]
    knot = basic_knot(ascii_codes, 64)
    return ''.join([hex(val).replace('0x', '').zfill(2)
                    for val in dense_hash(knot)])


if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.readline()
        p1_lengths = [int(x.strip()) for x in line.split(',')]
        p2_hash = string_knot_hash(line)
    p1_knot_hashed = basic_knot(p1_lengths)
    p1_ans = p1_knot_hashed[0] * p1_knot_hashed[1]
    print('Part 1 = %s*%s = %s' %
          (p1_knot_hashed[0], p1_knot_hashed[1], p1_ans))
    print('Part 2 = %s' % p2_hash)

def spinlock_insertions(steps, repeats):
    buffer = [0]
    pos = 0
    for i in range(1, 2018):
        pos = (pos + steps) % len(buffer)
        buffer = buffer[:pos + 1] + [i] + buffer[pos + 1:]
        pos += 1
    return buffer


def solve(steps):
    # p1
    p1_buffer = spinlock_insertions(steps, 2017)
    print('(P1) Value after 2017 in completed buffer: %s' %
          p1_buffer[p1_buffer.index(2017) + 1])
    # p2
    # Value 0 always at index 0 in buffer -> only need to watch for insertions
    # at index 1
    pos = 0
    for i in range(1, 50000000 + 1):
        pos = (pos + steps) % i
        if pos == 0:
            # would be inserted into index 1
            index_1_val = i
        pos += 1
    print('(P2) Value after 0 when 50000000 inserted: %s' % index_1_val)


if __name__ == '__main__':
    with open('input.txt') as f:
        steps = int(f.readline().strip())
    solve(steps)

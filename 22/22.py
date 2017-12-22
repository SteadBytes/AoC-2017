import os
import timeit


def part_1(infected, num_bursts=10000):
    # DOWN,LEFT,UP,RIGHT
    vectors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    d = num_infected = 0
    virus_loc = (0, 0)
    for _ in range(num_bursts):
        if virus_loc in infected:
            # infected, turn right
            d = (d - 1) % 4
            infected.remove(virus_loc)
        else:
            # clean, turn left
            d = (d + 1) % 4
            # becomes weakened
            infected.add(virus_loc)
            num_infected += 1
        virus_loc = (virus_loc[0] + vectors[d][0],
                     virus_loc[1] + vectors[d][1])
    return num_infected


def part_2(infected, num_bursts=10000000):
    CLEAN = 0
    INFECTED = 1
    WEAKENED = 2
    FLAGGED = 3
    state = {loc: INFECTED for loc in infected}
    # DOWN,LEFT,UP,RIGHT
    vectors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    d = num_infected = 0
    virus_loc = (0, 0)
    for _ in range(num_bursts):
        virus_state = state.get(virus_loc, CLEAN)
        if virus_state == CLEAN:
            # turn left
            d = (d + 1) % 4
            state[virus_loc] = WEAKENED
        elif virus_state == WEAKENED:
            # no turn
            state[virus_loc] = INFECTED
            num_infected += 1
        elif virus_state == INFECTED:
            # turn right
            d = (d - 1) % 4
            state[virus_loc] = FLAGGED
        elif virus_state == FLAGGED:
            # reverse direction
            d = (d + 2) % 4
            state[virus_loc] = CLEAN
        virus_loc = (virus_loc[0] + vectors[d][0],
                     virus_loc[1] + vectors[d][1])
    return num_infected


def solve(infected):
    print('Bursts causing a node to become infected:')
    print('(P1) %s' % part_1(infected.copy()))
    print('(P2) %s' % part_2(infected))


if __name__ == '__main__':
    infected = set()
    state = {}
    base_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base_dir, 'input.txt')) as f:
        lines = f.readlines()
    mid = len(lines) // 2
    for i, line in enumerate(lines):
        for j, ch in enumerate(line.strip()):
            if ch == '#':
                infected.add((i - mid, j - mid))
    solve(infected)

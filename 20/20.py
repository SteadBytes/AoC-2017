import os


def cross(a, b):
    """ Cross product of a and b
    """
    return [x + y for x, y in zip(a, b)]


def dist(particle):
    """ Manahattan distance of a particle from <0,0,0>
    """
    return sum([abs(x) for x in particle[0]])


def run_cycle(particles):
    for i, p in enumerate(particles):
        p[1] = cross(p[1], p[2])
        p[0] = cross(p[0], p[1])
    return particles


def remove_collisions(particles):
    positions = {}
    delete = []
    for i, p in enumerate(particles):
        pos = tuple(p[0])
        if pos in positions:
            delete += [i, positions[pos]]
        else:
            positions[pos] = i
    return [p for i, p in enumerate(particles) if i not in delete]


def part_1(particles):
    for _ in range(1000):
        run_cycle(particles)
        min_dist = min((d, i)
                       for i, d in enumerate([dist(p) for p in particles]))
    return min_dist[1]


def part_2(particles):
    for _ in range(1000):
        particles = remove_collisions(run_cycle(particles))
    return len(particles)


if __name__ == '__main__':
    particles = []
    base_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base_dir, 'input.txt')) as f:
        for line in f:
            p = [[int(y) for y in x.strip()[3:-1].split(',')]
                 for x in line.split(', ')]
            particles.append(p)
    # copy 2d list to not interfere w/p2
    print('(P1) %s' % part_1([p[:] for p in particles]))
    print('(P2) %s' % part_2(particles))

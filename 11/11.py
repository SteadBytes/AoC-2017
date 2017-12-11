# axial grid for hex grid representation:
# NW | N |
# ---+---+---
# SW |   |NE
# ---+---+---
#    | S | SE

VECTORS = {'n': (0, 1), 'ne': (1, 0), 'se': (1, -1),
           's': (0, -1), 'sw': (-1, 0), 'nw': (-1, 1)}


def hex_distance(a, b):
    """ Calculates manhattan distance between two points on an Axial grid
    representation of a hex grid

    Args:
        a (tuple): (x,y) coords of first point
        b (tuple): (x,y) coords of second point
    Returns:
        float
    """
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]) +
            abs((-a[0] - a[1]) - (-b[0] - b[1]))) / 2


def solution(path):
    """ Calculates shortest distance to reach the end point of a given path
    on a hex grid and the furthest disatnce reached at any point in the path.
    Args:
        path (:obj: `list` of str): Path step directions i.e ['ne','n','nw']
    Returns:
        tuple: (shortest_path_distance, max_point_distance)
    """
    pos = (0, 0)

    vector_path = [VECTORS[stepdir] for stepdir in path]

    max_from_start = 0
    for v in vector_path:
        pos = (pos[0] + v[0], pos[1] + v[1])
        max_from_start = max(max_from_start, hex_distance((0, 0), pos))
    if pos == (0, 0):
        # ended up back at start
        return 0
    # find shortest path from (0,0) to pos
    return hex_distance((0, 0), pos), max_from_start


if __name__ == '__main__':
    with open('input.txt') as f:
        child_path = f.readline().split(',')
    min_path_dist, max_dist_from_start = solution(child_path)
    print('Shortest path steps: %s' % min_path_dist)
    print('Furthest steps from start: %s' % max_dist_from_start)

import os


def rotate_90(grid):
    return list(zip(*grid[::-1]))


def flip_grid(grid):
    return [x[::-1] for x in grid]


def grid_tuple(grid):
    """ Generates 2d tuple from 2d grid (used for dict keys)
    """
    return tuple([tuple(row) for row in grid])


def enhance_grid(grid, rules):
    size = len(grid)
    if size % 2 == 0:
        # break into 2x2 squares->convert each to 3x3
        new_size = size // 2 * 3
        split = 2
        new_split = 3
    else:
        # break into 3x3 squares -> convert each to 4x4
        new_size = size // 3 * 4
        split = 3
        new_split = 4
    new_grid = [[0] * new_size for _ in range(new_size)]

    for i in range(size // split):
        for j in range(size // split):
            # subgrid row/col starting indexes
            subgrid_i = i * split
            subgrid_j = j * split
            subgrid = [row[subgrid_j:subgrid_j + split]
                       for row in grid[subgrid_i:subgrid_i + split]]
            # transform subgrid according to rules
            new_subgrid = rules[grid_tuple(subgrid)]

            # subgrid row/col starting indexes in larger enhanced grid
            subgrid_i = i * new_split
            subgrid_j = j * new_split
            # insert new_subgrid into enchanced grid
            for k in range(new_split):
                for l in range(new_split):
                    new_grid[subgrid_i + k][subgrid_j + l] = new_subgrid[k][l]
    return new_grid


def num_pixels_on(grid):
    return sum(x.count(True) for x in grid)


def solve(rules):
    grid = [[False, True, False],
            [False, False, True],
            [True, True, True]]
    for i in range(18):
        grid = enhance_grid(grid, rules)
        if i == 4:
            print('(P1) Pixels on after 5 iterations: %s' %
                  num_pixels_on(grid))
    print('(P2) Pixels on after 5 iterations: %s' %
          num_pixels_on(grid))


def add_rule(rules, new_rule):
    """ Adds possible rotations/flips of a given rule to rules dict.

    Args:
        rules (dict of tuple:list): Mapping from 2d tuple representation of a
            grid to its transformation
        new_rule (str): New rule to be added from puzzle input
            i.e '../.# => ##./#../... '
    Returns:
        None, mutates rules
    """
    inp, out = new_rule.split(' => ')
    inp = [[c == '#'for c in b] for b in inp.split('/')]
    out = [[c == '#'for c in b] for b in out.split('/')]
    # input patterns can be flipped or rotated to match
    flipped = flip_grid(inp)
    for _ in range(4):
        rules[grid_tuple(inp)] = out
        rules[grid_tuple(flipped)] = out
        inp = rotate_90(inp)
        flipped = rotate_90(flipped)


if __name__ == '__main__':
    # pattern replacement rules -> {input:output}
    rules = {}
    base_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base_dir, 'input.txt')) as f:
        for line in f:
            add_rule(rules, line)
    solve(rules)

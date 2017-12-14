from knot_hash import string_knot_hash


def used_squares(key_string):
    """ Finds indexes of all used squares in the 128x128 grid representing the
    disk, built from knot_hashes.

    Args:
        key_string (str): key string for knot hashing to build grid state
    Returns:
        list of (x,y): List of indexes (x,y) in the grid for each used square
    """
    used = []
    for i in range(128):
        row_hash = string_knot_hash(key_string + '-' + str(i))
        # slice to remove leading '0b'
        row_bits = bin(int(row_hash, 16))[2:].zfill(128)
        used += [(i, j) for j, bit in enumerate(row_bits) if bit == '1']
    return used


def total_regions(used_squares):
    """ Finds total number of regions - adjacent (not diagonal) used squares.
    Args:
        used_squares (list of (x,y)): List of used square indexes from
            `used_squares()` method
    Returns
        int: Total number of regions in the grid
    """
    count = 0
    while used_squares:
        q = [used_squares[0]]
        while q:
            (x, y) = q.pop()
            if (x, y) in used_squares:
                used_squares.remove((x, y))
                q += [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        count += 1
    return count


def solve(key_string):
    used = used_squares(key_string)
    print('(P1) Total used squares: %s' % len(used))
    print('(P2) Total regions: %s' % total_regions(used))


if __name__ == '__main__':
    with open('input.txt') as f:
        key_string = f.readline()
    solve(key_string)

from math import ceil, sqrt


def spiral_memory_p1(target):
    """
    Part 1
    Steps to center = steps to nearest horiz/verticalaxis
    crossing center + steps along axis to center (index of square currently on)

    Steps to axis: Reset a counter back to 1 when next square is entered(cycle)
    , reset to 0 again when a corner is reached (inner_offset).
    Difference between it and current_index is number of steps to nearest axis
    """
    # width/height of grid
    side_length = ceil(sqrt(target))

    if side_length % 2 == 0:
        side_length += 1

    current_index = (side_length - 1) / 2
    cycle = target - ((side_length - 2)**2)
    inner_offset = cycle % (side_length - 1)
    return current_index + abs(inner_offset - current_index)


def spiral_memory_p2(target):
    """
    Part 2 
    Anti clockwise Spiral grid (like p1) with 1 at center. Each value is the
    sum of the values in all adjacent squares including diagonals.abs
    Returns the first value in the grid which is **larger** than target
    """
    directions = [(1, 0), (1, -1), (0, -1), (-1, -1),
                  (-1, 0), (-1, 1), (0, 1), (1, 1)]
    x = y = dx = 0
    dy = -1
    matrix = {}
    while True:
        total = 0
        for v in directions:
            vx, vy = v
            if (x + vx, y + vy) in matrix:
                total += matrix[(x + vx, y + vy)]
        if total > int(target):
            return total
        if (x, y) == (0, 0):
            # first middle square
            matrix[(x, y)] = 1
        else:
            # set value of square to sum of adjacent squares
            matrix[(x, y)] = total

        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            # at edge of current section of spiral
            # change direction to build next edge
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


print(spiral_memory_p1(265149))
print(spiral_memory_p2(265149))

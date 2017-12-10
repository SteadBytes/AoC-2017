def solution_p1(maze):
    i = steps = 0
    while True:
        jump = maze[i]
        steps += 1
        if i + jump >= len(maze):
            break
        maze[i] += 1
        i += jump
    return steps


def solution_p2(maze):
    i = steps = 0
    while True:
        jump = maze[i]
        steps += 1
        if i + jump >= len(maze):
            break
        if jump >= 3:
            maze[i] -= 1
        else:
            maze[i] += 1
        i += jump
    return steps


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    maze = [int(x) for x in lines]
    # functions mutate list -> don't use both p1 and p2 in same execution
    # print(solution_p1(maze))
    print(solution_p2(maze))

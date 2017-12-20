import os


def solve(diagram):
    pos_x = diagram[0].index('|')
    pos_y = 0
    pos_contents = '|'
    direction = 'S'
    path_letters = []
    steps = 0
    while pos_contents != ' ':
        steps += 1
        if direction == 'N':
            pos_y -= 1
        elif direction == 'E':
            pos_x += 1
        elif direction == 'S':
            pos_y += 1
        elif direction == 'W':
            pos_x -= 1
        pos_contents = diagram[pos_y][pos_x]
        if pos_contents == '+':
            # '+' present at end of line in a direction
            if direction in ('N', 'S'):
                if diagram[pos_y][pos_x - 1] != ' ':
                    direction = 'W'
                else:
                    direction = 'E'
            else:
                if diagram[pos_y - 1][pos_x] != ' ':
                    direction = 'N'
                else:
                    direction = 'S'
        elif pos_contents.isalpha():
            path_letters.append(pos_contents)
    return path_letters, steps


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base_dir, 'input.txt')) as f:
        diagram = f.readlines()[:-1]  # last line is blank `\n`
    path_letters, steps = solve(diagram)
    print('(P1) Letters seen on packet path: %s' % ''.join(path_letters))
    print('(P2) Steps taken on packet path: %s' % steps)

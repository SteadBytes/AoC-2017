def apply_moves(programs, moves):
    """ Applies moves, in order, to the list of programs
    Args:
        programs (list of str): Program names i.e. ['a','b',...,'p']
        moves (list of str): Moves in the 'dance' i.e. ['s1','x3/4','pe/b']
    Returns:
        list: Program names in new order
    """
    for move in moves:
        if 's' in move:
            # Spin
            num = int(move[1:])
            programs = programs[-num:] + programs[:len(programs) - num]
        else:
            if 'x' in move:
                # Exchange
                i, j = [int(x) for x in move[1:].split('/')]
            else:
                # Partner
                i, j = [programs.index(x) for x in move[1:].split('/')]
            programs[i], programs[j] = programs[j], programs[i]
    return programs


def find_repeat_cycle(programs, moves):
    """ Finds the number of 'dance' repetitions needed to return the programs
    back to their initial state.

    Args:
        programs (list of str): Program names i.e. ['a','b',...,'p']
        moves (list of str): Moves in the 'dance' i.e. ['s1','x3/4','pe/b']
    Returns:
        int: Number of 'dance' repetitions to return to initial program state
    """
    init = programs[:]
    repeat_cycle = 0
    while True:
        programs = apply_moves(programs, moves)
        repeat_cycle += 1
        if programs == init:
            return repeat_cycle


def solve(programs, moves, num=1):
    """ Finds the positions of the programs after going through all given moves,
    num times.

    Args:
        programs (list of str): Program names i.e. ['a','b',...,'p']
        moves (list of str): Moves in the 'dance' i.e. ['s1','x3/4','pe/b']
        num (int): Number of times to repeat the 'dance'. Defaults to 1

    Returns:
        list: Program names in new order after `num` dances
    """
    if num > 1:
        num = num % find_repeat_cycle(programs[:], moves)
    for i in range(num):
        programs = apply_moves(programs, moves)
    return programs


if __name__ == '__main__':
    # programs = [chr(x) for x in range(97, 102)]  # for example input
    programs = [chr(x) for x in range(97, 113)]  # for full input
    with open('input.txt') as f:
        moves = f.readline().split(',')

    print('(P1) Positions after 1 repeat: %s' %
          ''.join(solve(programs[:], moves)))
    print('(P2) Positions after 1000000000 repeats: %s' %
          ''.join(solve(programs[:], moves, 1000000000)))

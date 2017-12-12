def solution(banks):
    cycles = 0
    states = []
    state = banks
    while state not in states:
        states.append([x for x in state])
        max_val = max(state)
        i = state.index(max_val)
        state[i] = 0
        for j in range(1, max_val + 1):
            state[(i + j) % len(state)] += 1
        cycles += 1
    return cycles


if __name__ == '__main__':
    with open('input.txt') as f:
        banks = [int(x) for x in f.readline().split()]
    # banks = [0, 2, 7, 0]
    print(solution(banks))  # part 1
    # part 2: banks list mutated by first call - already in a seen state,
    # ready to find size of infinite loop by running p1 again
    print(solution(banks))

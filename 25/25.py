import os
import re


def solve(states, start, steps):
    cursor_pos = 0
    current_state = start
    set_slots = set()

    for _ in range(steps):
        if cursor_pos in set_slots:
            inst = states[current_state][1]
            if inst[0] == '0':
                set_slots.remove(cursor_pos)
        else:
            inst = states[current_state][0]
            if inst[0] == '1':
                set_slots.add(cursor_pos)
        if inst[1] == 'left':
            cursor_pos -= 1
        else:
            cursor_pos += 1
        current_state = inst[2]
    print(len(set_slots))


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))

    RULE_RE = r"""\
In state (.):
  If the current value is 0:
    - Write the value (.)\.
    - Move one slot to the (\w+)\.
    - Continue with state (.)\.
  If the current value is 1:
    - Write the value (.)\.
    - Move one slot to the (\w+)\.
    - Continue with state (.)\."""

    with open(os.path.join(base_dir, 'input.txt')) as f:
        start = re.search(r'Begin in state (.)\.', f.readline()).group(1)
        steps = int(re.search(r'after (\d+) steps', f.readline()).group(1))

        rules = re.findall(RULE_RE, f.read())
        states = {}
        for rule in rules:
            states[rule[0]] = [rule[1:4], rule[4:]]
    solve(states, start, steps)

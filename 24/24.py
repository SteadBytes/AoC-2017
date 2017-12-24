import os


def bridge_search(start, connection, components):
    """ Recursively find all possible bridges
    """
    connecting = [c for c in components if connection in c]
    if not connecting:
        return [start]
    bridges = []
    for comp in connecting:
        remaining = components[:]
        remaining.remove(comp)
        new_connection = comp[0] if comp[0] != connection else comp[1]
        bridges += bridge_search(
            start + [comp], new_connection, remaining)
    return bridges


def bridge_strength(bridge):
    return sum([sum(x) for x in bridge])


def bridge_score(bridge):
    """ Returns tuple of bridge (strength, length)
    """
    return (bridge_strength(bridge), len(bridge))


def solve(components):
    bridges = bridge_search([], 0, components)
    bridge_scores = [bridge_score(bridge) for bridge in bridges]
    strongest = max(bridge_scores)
    # maximum ordered first by length, then by strength
    longest = max(bridge_scores, key=lambda x: (x[1], x[0]))
    print('(P1): Max strength =', strongest)
    print('(P2): Max length =', longest[1], 'strength=', longest[0])


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base_dir, 'example_input.txt')) as f:
        components = [[int(x) for x in y.split('/')] for y in f.readlines()]
    solve(components)

def find_group_dfs(graph, start):
    """ Uses depth first search to determine the nodes in the group
    containing `start`.abs
    Args:
        graph (dict of str: list of str): Mapping from nodes to connections
        start (str): Node to find group for
    Returns:
        set: Nodes in group containing `start`
    """
    if start not in graph:
        return None
    q = [start]
    visited = set()
    while q:
        v = q.pop()
        if v not in visited:
            visited.add(v)
            for conn in graph[v]:
                q.append(conn)
    return visited


if __name__ == '__main__':
    graph = {}
    with open('input.txt') as f:
        for line in f:
            line = [x.strip() for x in line.replace(' <-> ', ',').split(',')]
            graph[line[0]] = line[1:]

    # Part 1
    group_0 = find_group_dfs(graph, '0')
    print('Part 1 - Size of group containing \'0\': %s' % len(group_0))

    # Part 2
    total_groups = 1  # group_0 already found
    remaining = {v for v in graph if v not in group_0}
    while remaining:
        v = remaining.pop()
        group = find_group_dfs(graph, v)
        remaining -= group
        total_groups += 1
    print('Part 2 - Total number of groups: %s' % total_groups)

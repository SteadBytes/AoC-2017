def solution_p1(children):
    """ Finds root node
    """
    for prg in children:
        root = True
        for prg2 in children:
            if prg != prg2 and prg in children[prg2]:
                root = False
                break
        if root:
            return prg


def dfs(children, weights, root):
    """ DFS that tracks expected weights of nodes to find the single node
    which needs weigth changing.
    """
    exp = None
    s = weights[root]
    if root in children:
        for child in children[root]:
            w = dfs(children, weights, child)
            s += w
            if exp is None:
                exp = w
            elif exp != w:
                print('Expected child, %s to have weight %s, has weight, %s' %
                      (child, exp, w))
                print(w - weights[child])
    return s


if __name__ == '__main__':
    weights = {}
    children = {}
    with open('input.txt') as f:
        for l in f:
            name = l[:l.index(' ')]
            weight = l[l.index('(') + 1:l.index(')')]
            weights[name] = int(weight)
            if '>' in l:
                children[name] = l[l.index('>') + 2:].replace(',', '').split()
    root = solution_p1(children)
    # child in first line of output from dfs() needs weight changing
    # difference = expected - weight (in line of output from dfs())
    # answer = original weight of child in input.txt minus difference
    print(dfs(children, weights, root))
    # for input.txt, dfs() gives:
    # >>> Expected child, utnrb to have weight 1951, has weight, 1960
    # >>> 1422
    # >>> Expected child, lahahn to have weight 8603, has weight, 8612
    # >>> 5862
    # >>> Expected child, zoibnsq to have weight 82373, has weight, 82364
    # >>> 82356
    # >>> Expected child, mblsyx to have weight 82373, has weight, 82364
    # >>> 31206
    # >>> Expected child, vkkwtq to have weight 82373, has weight, 82364
    # >>> 21132
    # >>> Expected child, cwluofv to have weight 82373, has weight, 82364
    # >>> 29799
    # >>> 411871
    # utnrb difference = 1960-1951 = 9
    # answer = weights[utnrb]-9 = 529
    # used `sls utnrb .\input.txt -ca` in powershell to get original input
    # then calculate answer 'by hand'

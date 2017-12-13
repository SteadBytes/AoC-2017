def total_penalty(layers):
    """ Starting at time 0, calculates the total penalty for passing through
    the given firewall layout. Caught at a layer penalty = depth*layer

    Args:
        layers (dict of int:int): Mapping from depth:range for layers
    Returns
        int: total penalty
    """
    penalty = 0
    for layer, depth in layers.items():
        if layer % ((depth - 1) * 2) == 0:
            penalty += layer * depth
    return penalty


def delay_sufficient(layers, delay):
    """ Returns whether a given delay will result in no penalty
    Args:
        layers (dict of int:int): Mapping from depth:range for layers
        delay (int): Size of delay
    Returns
        bool
    """
    for layer, depth in layers.items():
        if (layer + delay) % (2 * depth - 2) == 0:
            return False
    return True


def find_delay(layers):
    """ Calculates the minimum delay required before beginning traversal of the
    firewall for no penalty to be incurred.
    Args:
            layers (dict of int:int): Mapping from depth:range for layers
            delay (int): Size of delay
    Returns:
        int: Size of minium delay required
    """
    delay = 1
    while True:
        if delay_sufficient(layers, delay):
            break
        else:
            delay += 1
    return delay


if __name__ == '__main__':
    layers = {}
    with open('example_input.txt') as f:
        for line in f:
            layer_depth, layer_range = [int(x.strip())
                                        for x in line.split(':')]
            layers[layer_depth] = layer_range
        print('(P1) Total penalty: %s' % total_penalty(layers))
        print('(P2) Minimum delay for no penalty: %s' % find_delay(layers))

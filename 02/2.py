def list_range(a):
    """Returns the range of an a list of numbers
    Args:
        a (:obj:`list` of :obj:`int` or `float`)
    Returns:
        `int` or `float`: range of the values in a
    """
    return (max(a) - min(a))


def list_evenly_divide(a):
    """Returns result of dividing the two evenly divisible numbers in a list

    Intended use for a list with **only two evenly divisble numbers**
    Args:
        a (:obj:`list` of :obj:`int` or `float`)
    Returns:
        `int` or `float`: x/y where x,y are elements of list a and x%y==0
    """
    prods = [(x, y) for x in a for y in a if x != y]
    for x, y in prods:
        if x % y == 0:
            return x / y


if __name__ == '__main__':
    # user input number of lines in the spreadsheet
    n = int(input().strip())
    checksum = 0  # part 1
    evenly_divisible_sum = 0  # part 2

    for _ in range(n):
        a = [int(x) for x in input().strip().split()]
        checksum += list_range(a)  # part 1
        evenly_divisible_sum += list_evenly_divide(a)  # part 2

    print(checksum)
    print(evenly_divisible_sum)

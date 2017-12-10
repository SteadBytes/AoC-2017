def inverse_captcha(s):
    """ Returns the sum of all digits that match the next digit in the string. 
    The list is **circular**, so the digit after the last digit is the first 
    digit in the list.

    Args:
        s(str): String of digits i.e '91212129'
    Returns:
        int
    """
    n = len(s)
    res = 0
    for i, ch in enumerate(s):
        if ch == s[(i + 1) % n]:
            res += int(ch)
    return res


def inverse_captcha_2(s):
    """ Returns the sum of all digits that match the digit halfway around the
    circular list. If s contains 10 items, only include in the sum if
    the digit 10/2 = 5 steps forward matches it.

    Args:
        s(str): String of digits i.e '91212129'
    Returns:
        int
    """
    n = len(s)
    mid = int(n / 2)
    res = 0
    for i, ch in enumerate(s):
        if ch == s[(i + mid) % n]:
            res += int(ch)
    return res


if __name__ == '__main__':
    s = input().strip()
    print(inverse_captcha(s))
    print(inverse_captcha_2(s))

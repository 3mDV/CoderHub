def root_check(sqr, num):
    # write your code here
    num = float(num)
    if (num ** 2) == sqr:
        return int(num)
    else:
        return int(0)


def root_check1(sqr: int, num: float): return int(num) if (num ** 2) == sqr else int(0)  # One-line function from

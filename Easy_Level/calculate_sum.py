from typing import List


def calculate_sum(lst: List[int]) -> int:
    # write your code here ^_^
    if lst.count(7) > 0:
        return int(sum(lst[:lst.index(7)]))
    else:
        return int(sum(lst))


def calculate_sum1(lst: List[int]) -> int:
    return int(sum(lst[:lst.index(7)])) if lst.count(7) > 0 else int(sum(lst))
    # int(sum(lst[0:index])

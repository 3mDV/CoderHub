from typing import List
def oddsVsEvens(num: int) -> str:
    # write your code here ^_^
    odd = 0
    even = 0
    for i in [int(n) for n in str(num)]:
        if (i % 2) == 0:
            even = even + i
        else:
            odd = odd + i
    if odd > even:
        return "odd"
    elif odd < even:
        return "even"
    else:
        return "equal"


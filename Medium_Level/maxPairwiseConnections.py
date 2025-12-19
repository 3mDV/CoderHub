from typing import List
def maxPairwiseConnections(s: str) -> int:
    # write your code here ^_^
    count = 0
    a = s.count("A")
    b = s.count("B")
    x = s.count("X")
    y = s.count("Y")
    if a == b:
        count += a

    if x == y:
        count += x

    return count
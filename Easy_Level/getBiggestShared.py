from typing import List
def getBiggestShared(a: List[int], b: List[int]) -> int:
    # write your code here ^_^
    result = [i for i in (a + b) if (a + b).count(i) > 1]
    return max(result)
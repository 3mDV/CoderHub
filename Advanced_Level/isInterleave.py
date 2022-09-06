from typing import List
def isInterleave(A: str, B: str, C: str) -> bool:
    # write your code here ^_^
    if ''.join(sorted((A + B))) == ''.join(sorted(C)):
        return True
    else:
        return False
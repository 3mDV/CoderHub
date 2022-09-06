from typing import List
def countdown(num: int) -> List[int]:
    # write your code here ^_^
    result = []
    for i in range(num, 0,-3):
        if i % 2 == 0 and i != num:
            result.append(i)
        else:
            pass
    result.sort()
    return result if len(result) > 0 else [0]
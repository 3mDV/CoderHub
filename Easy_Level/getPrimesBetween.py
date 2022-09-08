from typing import List
def getPrimesBetween(a: int, b: int) -> List[int]:
    # write your code here ^_^
    result = []
    for num in range(a, b + 1):
        for i in range(1, int(num ** .5) + 1):
            if (num % i) == 0 and (i != num) and (i != 1):
                result.remove(num) if result.count(num) > 0 else result.copy()
                break
            elif num > 1:
                result.append(num)
                if result.count(num) > 1:
                    result = list(set(result))
                else:
                    continue

    return sorted(result)

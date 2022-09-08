from typing import List
def primes_nums(numbers: List[int]) -> List[int]:
    # write your code here ^_^
    result = numbers.copy()
    for num in numbers:
        if num > 2:
            flag = True
            i = int((num ** .5) + 1)
            while flag and i > 1:
                if (num % i) == 0:
                    result.remove(num)
                    flag = False
                else:
                    i -= 1
        else:
            continue
    return result

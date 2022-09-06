from typing import List
def tribonacci(num: int) -> List[int]:
    # write your code here ^_^
    tribonacci_numbers = [1, 1, 1]
    for i in range(num):
        if num > 2:
            tribonacci_numbers.append(sum(tribonacci_numbers[i:]))

    return list(tribonacci_numbers[:num])
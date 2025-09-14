from typing import List
def convertToBase7(num: int) -> str:
    # write your code here ^_^
    result = ""
    state = abs(num) == num
    num = abs(num)
    for i in range(0,(num % 7)+1):
        result = str(num % 7) + result
        num = num // 7
        print(i)
    return result if state else f"-{result}"

# print(convertToBase7(100))
print(convertToBase7(-7))
# print(convertToBase7(0))
# print(convertToBase7(49))
print(int("-7", 7))
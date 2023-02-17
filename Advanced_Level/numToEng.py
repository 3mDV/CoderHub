from typing import List


def numToEng(n: int) -> str:
    # write your code here ^_^
    num1 = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninty"}

    if n <= 19:
        return num1.get(n)
    elif 19 <= n < 100:
        n = str(n)
        return f"{num1.get(int(n[0] + '0'))}-{num1.get(int(n[-1]))}" if n[-1] != "0" else f"{num1.get(int(n[0] + '0'))}"
    elif str(n)[1:] == "00":
        n = str(n)
        return f"{num1.get(int(n[0]))} hundred"

    elif 99 < n < 1000:
        n = str(n)
        if 0 < int(n[1:]) < 10:
            return f"{num1.get(int(n[0]))} hundred {num1.get(int(n[-1]))}"
        elif 9 < int(n[1:]) <= 20:
            return f"{num1.get(int(n[0]))} hundred {num1.get(int(n[1:]))}"
        elif 20 < int(n[1:]) < 100:
            return f"{num1.get(int(n[0]))} hundred {num1.get(int(n[1:]))}"

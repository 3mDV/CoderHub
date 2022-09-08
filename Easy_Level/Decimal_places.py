def Decimal_places(num):
    # write your code here
    find = num.find(".")
    if find > 0:
        return len(num[find + 1:])
    else:
        return int(0)

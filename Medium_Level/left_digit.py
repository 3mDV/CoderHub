def left_digit(txt):
    # write your code here
    txt = list(txt)
    result = []
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for check in txt:
        if check in str(numbers):
            result.append(check)
    return int(result[0])
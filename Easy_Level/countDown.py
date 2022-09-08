def countDown(number):
    # write your code here
    result = []
    for num in range(int(number),-1,-1):
        result.append(num)

    result = str(result).strip("[]").replace(",", "")
    return result


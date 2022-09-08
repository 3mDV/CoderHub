def operation(num1: int, num2: int) -> str:
    # write your code here ^_^
    if (num1 / num2) == 24:
        return str("divided")
    elif (num1 * num2) == 24:
        return str("multiplied")
    elif (num1 + num2) == 24:
        return str("added")
    elif (num1 - num2) == 24:
        return str("subtracted")
    else:
        return str("None")


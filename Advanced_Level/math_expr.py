def math_expr(expr: str) -> bool:
    # write your code here ^_^
    opretion = ['+', '-', '/', '*']
    result = []
    for i in expr:
        if i.isdigit() == True or i in opretion:
            result.append(True)
        else:
            result.append(False)
    return True if not(False in result) else False
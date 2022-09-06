from typing import List
def postFix(expr: str) -> int:
    # write your code here ^_^
    stack = []
    expr1 = expr.split()
    for i in expr1:
        if i.isdigit() == True:
            stack.append(i)
        else:
            operation = i
            if len(stack) > 1:
                f_unm = stack[-2]
                s_num = stack[-1]
                result = str(eval(f_unm + operation + s_num))
                stack.remove(f_unm)
                stack.remove(s_num)
                stack.append(result)

    return int(float(stack[0]))
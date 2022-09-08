def input_type(value):
    # write your code here
    num = [str(i) for i in range(10)]
    if value.count(".") > 0:
        return "double"
    elif value[0] in num and value.count(".") == 0:
        return "integer"
    else:
        return "string"

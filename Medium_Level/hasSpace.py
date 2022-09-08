def hasSpace(str):
    # write your code here
    if str.count(' ') == 0:
        return str
    else:
        return str.replace(' ', '#')

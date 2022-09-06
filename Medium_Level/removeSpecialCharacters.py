from typing import List
def removeSpecialCharacters(strParam: str) -> str:
    # write your code here ^_^
    result = ''
    for i in strParam:
        if i.isupper() == True or i.islower() == True or i.isspace() == True or i == "-" or i == "_":
            result = result + i
        else:
            pass
    return result

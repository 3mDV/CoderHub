from typing import List
def middle_char(word: str) -> str:
    # write your code here ^_^
    if len(word) < 2:
        return str(word)
    elif len(word) % 2 == 0:
        return str(word[int(len(word)/2)-1:int(len(word)/2)+1])
    elif len(word) % 2 != 0:
        return str(word[int((len(word) / 2))])

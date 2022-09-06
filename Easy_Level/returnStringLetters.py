from typing import List
def returnStringLetters(string1: str, string2: str) -> int:
    # write your code here ^_^
    return int(len(string1) if len(string1) > len(string2) else len(string2))
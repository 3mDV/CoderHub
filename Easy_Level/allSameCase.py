from typing import List

def allSameCase(word: str) -> bool:
    if word.isupper() == True or word.islower() == True:
        return True
    return False

from typing import List
def namesSort(namesArray: List[str], order: str) -> List[str]:
    # write your code here ^_^
    if order == "ASC":
        namesArray.sort(reverse=False)
        return namesArray
    else:
        namesArray.sort(reverse=True)
        return namesArray
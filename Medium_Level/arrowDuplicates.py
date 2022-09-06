def arrowDuplicates(word: str) -> str:
    # write your code here ^_^
    result = ""
    word = word.lower()
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            result = result + "<"
        else:
            result = result + ">"
    return str(result)
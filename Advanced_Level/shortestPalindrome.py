def shortestPalindrome(word: str) -> str:
    first = 0
    last = len(word) - 1
    while last > 0:
        if word[last] == word[first]:
            first += 1
            last -= 1
            continue
        elif word[last] != word[first]:
            word = word[:first] + word[last] + word[first:]
            last += 1
            continue
    return word

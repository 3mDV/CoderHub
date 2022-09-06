from typing import List
def find_prefix(words: List[str], text: str) -> List[str]:
    # write your code here ^_^
    result = []
    text = text.title()
    for i in range(len(words)):
        if words[i].title()[:len(text)] == text:
            result.append(words[i])
        else:
            pass
    return list(result) if len(result) > 0 else ["No matches found"]
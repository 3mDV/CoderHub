from typing import List
def str_len_comparison(words List[str]) - bool
    # write your code here ^_^
    if len(words)  1
		check = set(map(lambda xlen(x),words))
        return True if len(check) == 1 else False
    else
        return False
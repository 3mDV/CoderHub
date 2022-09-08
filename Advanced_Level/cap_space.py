def cap_space(txt):
    # write your code here
    txt = list(txt)
    for i in range(len(txt)):
        if txt[i].isupper():
            txt[i] = txt[i].lower()
            txt.insert(txt.index(txt[i]), " ")
        else:
            pass
    return ''.join(txt).lower()


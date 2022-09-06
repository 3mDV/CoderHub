def missingLetter(txt):
    # write your code here
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    txt = list(txt)
    find = char.index(txt[0])


    for i in range(len(txt)):
        if txt[i] != char[find]:
            
            find += 1
            return char[find-1]
            # print(char[find])
            
        find+=1

    return "No Missing Letter"

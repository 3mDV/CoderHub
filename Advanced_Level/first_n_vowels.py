def first_n_vowels(phrase, n):
    # write your code here
    import re
    vowels = re.findall(r'[aeiou|AEIOU]', phrase)
    result = ''.join(i for i in vowels)
    if len(vowels) >= n:
        return result[:n]
    else:
        return "invalid"


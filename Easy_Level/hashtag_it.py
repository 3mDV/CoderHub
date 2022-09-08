def hashtag_it(array):
    # write your code here
    for i in range(len(array)):
        array[i] = '#{} '.format(array[i])
    return "".join(array)

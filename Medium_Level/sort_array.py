def sort_array(array, type):
    # write your code here
    if type == "B":
        array.sort(reverse=True)
        return array
    elif type == "S":
        array.sort(reverse=False)
        return array


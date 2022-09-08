def unique(arr):
    # write your code here
    result = []
    for i in range(len(arr)):
        if arr.count(arr[i]) > 1:
            pass
        else:
            result.append(arr[i])
    return result


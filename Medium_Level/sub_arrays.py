def sub_arrays(arr1, arr2):
    # write your code here
    result = []
    for i in range(len(arr1)):
        result.append(arr2[i] - arr1[i])
    return result

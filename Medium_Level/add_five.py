def add_five(arr):
  # write your code here
  for i in range(len(arr)):
    if len(arr) > 0:
      arr[i]+='5'
    else:
      return []
  return arr

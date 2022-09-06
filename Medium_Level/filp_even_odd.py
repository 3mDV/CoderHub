def filp_even_odd(array):
  # write your code here
  for i in range(len(array)):
    if array[i] % 2 == 0:
      array[i]+=1
    elif array[i] % 2 != 0:
      array[i]-=1
  return array
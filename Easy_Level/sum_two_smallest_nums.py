def sum_two_smallest_nums(arr):
  # write your code here
  arr.sort(reverse=False) # reverse False to smaller to Larger
  total = arr[0] + arr[1]
  return sum(arr[:2]) # or total same output
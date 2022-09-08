def cumulative_sum(arr):
	# write your code here
	empty = 0
	result = []
	for i in range(len(arr)):
		empty += arr[i]
		result.append(empty)
	return result


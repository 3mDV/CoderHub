
def match_arrays(array1, array2):
	# write your code here
	array1.sort(reverse=True)
	array2.sort(reverse=True)
	if array1 == array2:
	  return "true"
	else:
	  return "false"
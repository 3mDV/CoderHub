def longestZero(str) -> str:
	# write your code here
	str = str.split('1')
	mx = max(str, key=len)
	if "0" in mx:
		return mx
	else:
		return " "

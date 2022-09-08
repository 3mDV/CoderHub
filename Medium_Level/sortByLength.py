def sortByLength(txt):
	# write your code here
	s = txt.split(' ')
	s.sort(key=len)
	return ' '.join(i for i in s)

def bin_to_oct(b):
	# write your code here
	binary = int(str(b),2)
	octal = oct(binary)[2:]
	return int(octal)
def oct_to_bin(octal):
	# write your code here
	octal = int(str(octal), 8)
	binary = bin(octal)[2:]
	return binary



def oct_to_hex(oct):
	# write your code here
	octal = int(str(oct), 8)
	hexadecimal = hex(octal)[2:]
	return hexadecimal.upper()

def addStrNums(num1, num2) -> str:
	# write your code here
	try:
	  int(num1)
	  int(num2)
	  return str(int(num1) + int(num2))
	except ValueError:
	  return str(-1)
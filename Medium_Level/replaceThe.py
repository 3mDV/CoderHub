def replaceThe(txt):
	# write your code here
	find = txt.find("the")
	character = ["a", "e", "i", "o", "u"]
	if txt[find + 4] in character:
		text = txt.replace("the", "an")
		return text
	else:
		text = txt.replace("the", "a")
		return text

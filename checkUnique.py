def func_unique(string):
	alphaSet = set(list(string))
	if len(alphaSet) == len(string):
		return True

	return False


if __name__ == '__main__':
	string  = input("Input String: ")
	unique = func_unique(string)
	print (unique)
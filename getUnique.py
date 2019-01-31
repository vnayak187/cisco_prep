def getUnique(elements):
	eleSet = set(elements)
	return len(list(eleSet))

if __name__ == '__main__':
	string = input("Enter list elements seperated by space: ")
	elements = string.split()
	unique  = getUnique(elements)

	print (unique)
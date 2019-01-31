def checkaZero(string):
	count = 0

	for i in range(len(string)):
		if i > 0:
			if string[i] == '0':
				if string[i-1] == 'a':
					count += 1

	return count



if __name__ == '__main__':
	string = input("Input String: ")

	count = checkaZero(string)

	print (count)
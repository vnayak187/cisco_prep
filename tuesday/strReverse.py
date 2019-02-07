#function for reversing a string

def strReverse(text):
	if not text:
		return ''

	n = len(text)
	textList = list(text)

	for i in range(n//2):
		temp = textList[i]
		textList[i] = textList[n-i-1]
		textList[n-i-1] = temp

	result = ''.join(textList[i] for i in range(n))

	return result


if __name__ == "__main__":
	while True:
		string = input("Enter a string or Enter 0 to exit: ")
		if string.strip() == "0":
			break
		result = strReverse(string)
		print (result)
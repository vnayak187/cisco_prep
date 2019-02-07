#function for calculating factorial

def factorial(num):
	if num == 0 or num == 1:
		return 1

	result = num * factorial(num - 1)

	return result


if __name__ == "__main__":
	while True:
		n = input("Enter a non negative integer or enter quit to exit: ")
		if n == 'quit':
			break

		result = factorial(int(n))

		print (result)
def funcAssert(num):
	assert num in range(-5,6), "Number is not in range [-5, 5]"

	return True


if __name__ == "__main__":
	num = input("Enter a number: ")

	funcAssert(int(num))

	print ("Number is within range")


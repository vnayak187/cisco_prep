# function for converting decimal to binary
def decToBin(num):
	y = int(num)
	res = []
	if y == 0:
		return '0'

	while y:
		div = y//2
		mod = y%2
		res.append(str(mod))
		y = div

	result = ''.join(res[i] for i in range(len(res)-1, -1, -1))

	return result

if __name__ == '__main__':
	while True:
		n = input("Enter a non-negative integer or enter quit to exit: ")
		if n.strip() == 'quit':
			break

		res = decToBin(int(n))

		print (res)

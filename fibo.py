def fibo(res, n):
	if n == 1 or n == 2:
		res[n-1] = 1
		return 1
	fibo_n = fibo(res, n-1) + fibo(res, n-2)

	res[n-1] = fibo_n
	return fibo_n


if __name__ == "__main__":
	while True:
		n = input("Enter integer greater than 0 or enter 0 to exit: ")
		if int(n) == 0:
			break
		fibo_series = [0]*int(n)
		fibo(fibo_series, int(n))
		print (fibo_series)
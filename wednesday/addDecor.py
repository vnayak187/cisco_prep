# Addition with decorator

import re

def validateNums(num):
	exp = re.compile(r'^\-?\d*\.?\d+$')

	if exp.match(num):
		print (num)
		return True

	return False


def addDecor(func):
	def wrapper(*args):
		if validateNums(args[0]) and validateNums(args[1]):
			print (args)
			func(*args)
		else:
			print ("Numbers are not valid")
			pass

	return wrapper





@addDecor
def add(num1,num2):
	result = float(num1) + float(num2)
	print ("{} + {} = {}".format(num1, num2, result))


if __name__ == "__main__":
	num1 = input("Enter first number: ")
	num1 = num1.strip()

	num2 = input("Enter second number: ")
	num2 = num2.strip()

	add(num1, num2)


	

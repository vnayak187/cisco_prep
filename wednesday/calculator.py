import re

squareNums = map(lambda x: x**2,filter(lambda x: x % 2 == 0, range(1,101)))

class ParentCalc(object):
	def __init__(self):
		self.num1 = -1
		self.num2 = -1

	def validateNums(self):
		if self.num2 == 0:
			return False

		return True

	def acceptInput(self):
		exp = re.compile(r'\-?[0-9]+($|\.[0-9]+)')
		while True:
			op = input("Enter a operation (+, -, *, /) or Enter 0 to exit: ")
			if op.strip() == "0":
				return []
			if op.strip() in ('+', '-', '*', '/'):
				break

		while True:
			num1 = input("Enter 1st integer: ")
			if exp.search(num1.strip()):
				self.num1 = float(num1)
				break

		while True:
			num2 = input("Enter 2nd integer: ")
			if exp.search(num2.strip()):
				self.num2 = float(num2)
				break


		return num1, num2, op

class Calc(ParentCalc):
	def add(self):
		return self.num1 + self.num2

	def sub(self):
		return self.num1 - self.num2

	def mul(self):
		return self.num1 * self.num2

	def div(self):
		if self.validateNums():
			return self.num1 / self.num2

		return None










if __name__ == "__main__":
	print (list(squareNums))
	while True:
		calc = Calc()
		inputs = calc.acceptInput()
		if not inputs:
			break
		num1 = inputs[0]
		num2 = inputs[1]
		op = inputs[2]
		
		switcherDict = {'+':calc.add(),'-':calc.sub(), '*':calc.mul(), '/':calc.div()}

		func = switcherDict.get(op)
		output = func
		if output is None:
			print ("Division by 0 error")
		else:
			print ("{} {} {} = {}".format(num1, op, num2, output))

class Parent(object):
	def __init__(self):
		self.id = 100

	def getValue(self):
		return "Parent Value and ID:{0}".format(self.id)

	def getID(self):
		return self.id


class Child(Parent):
	def getID(self):
		return self.id + 1



if __name__ == '__main__':
	p = Parent()
	c = Child()

	print ("calling parent getValue function from child, child value: {0}".format(c.getValue()))
	print ("calling overriden getID function from child,  child id: {0}".format(c.getID()))

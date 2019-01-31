def getCases(string):
	caseDict = dict()
	caseDict['uc'] = 0
	caseDict['lc'] = 0

	for i in range(len(string)):
		ascii = ord(string[i])
		if ascii >= 65 and ascii <= 90:
			caseDict['uc'] += 1
		elif ascii >= 97 and ascii <= 122:
			caseDict['lc'] += 1


	return caseDict



if __name__ == '__main__':
	string = input("Input String: ")
	caseDict = getCases(string)
	print ("UPPERCASE COUNT: {0}".format(caseDict['uc']))
	print ('lowercase count: {0}'.format(caseDict['lc']))
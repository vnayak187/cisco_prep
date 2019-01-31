import re

def findTS(filePath):
	res = []
	tsList = []
	with open(filePath) as file:
		for line in file:
			print (line)
			tsList = re.findall(r'time_sample\[?[0-9]*\]?', line)
			if tsList:
				for ts in tsList:
					res.append(ts)

	return res



if __name__ == '__main__':
	result = findTS("input_file.txt")
	print (result)

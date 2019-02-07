import os
import sys
import re

# Function for recursive dir traversal

def recurseDir(path):
	result = []

	for root, subdirs, files in os.walk(path):

	    for file in os.listdir(root):

	        filePath = os.path.join(root, file)

	        if os.path.isdir(filePath):
	            pass

	        else:
	            exp = re.compile(r'hcl')
	            if re.search(str(file)):
	            	result.append(file)


	return result



if __name__ == "__main__":
	path = input("Enter path to file: ")
	result = recurseDir(path)

	if not result:
		print ("No files with hcl found")

	else:
		print (result)

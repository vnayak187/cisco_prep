def incrementIP(ipAddr):
	ipList = ipAddr.split('.')
	ipList = [int(ipList[i]) for i in range(len(ipList))]
	carry = 1

	for i in range(len(ipList)-1,-1,-1):
		if ipList[i] + carry > 255:
			ipList[i] = 255
			carry = 1
		else:
			ipList[i] = ipList[i] + carry
			carry = 0

	newIP = ".".join([str(ipList[i]) for i in range(len(ipList))])

	return newIP


if __name__ == '__main__':
	ipAddr = input("Enter IP address to increment: ")
	validateIP = ipAddr.split('.')
	valid = True
	for i in range(len(validateIP)):
		if int(validateIP[i]) < 0 or int(validateIP[i]) > 255:
			valid = False
			break

	if valid:
		newIP = incrementIP(ipAddr)
		print ("Incremented IP: "+ newIP)
	else:
		print ("IP Addr id invalid")

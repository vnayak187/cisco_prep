import datetime as dt

#function for finding time difference

def dateTimeDiff(time1, time2):
	time1 = dt.datetime.strptime(time1, '%d/%m/%Y %H:%M:%S')
	print  (time1)
	time2 = dt.datetime.strptime(time2, '%d/%m/%Y %H:%M:%S')
	print (time2)
	res = ''

	if time1 > time2:
		res = time1 - time2
	else:
		res = time2 - time1

	

	secs = res.seconds%60
	mins = int(res.seconds/(60)%60)
	hrs = int(res.seconds/(60 * 60)%24) + int(res.days*24)

	return (hrs, mins, secs)


if __name__ == "__main__":
	
	time1 = input("Enter first date(dd/mm/yyyy) time(hh:mm:ss): ")
	time1 = time1.strip()

	time2 = input("Enter second date(dd/mm/yyyy) time(hh:mm:ss): ")
	time2 = time2.strip()

	hrs, mins, secs = dateTimeDiff(time1, time2)

	print ("time Differs is {} hrs {} mins {} secs".format(hrs, mins, secs))










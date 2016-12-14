import os, datetime, time

# determine if the curren time in within a given time range (24 hour clock)
def inrange(self, starthour, startmin, stophour, stopmin):
	# Set the now time to an integer that is hours * 60 + minutes
	no = datetime.datetime.now()
	now = no.hour * 60 + no.minute 
	
	# Set the start time to an integer that is hours * 60 + minutes
	star = datetime.time(starthour, startmin)
	start = star.hour * 60 + star.minute 
	
	# Set the stop time to an integer that is hours * 60 + minutes
	sto = datetime.time(stophour, stopmin)
	stop = sto.hour * 60 + sto.minute

	# handle midnight by adding 24 hours to stop time and now time
	if stop < start:
		stop += 1440
		now += 1440 
	#see if we are in the range
	if start <= now < stop:
		return True
	return False


def main(self):

	while True:
		if inrange(self, 13, 30, 13, 31):
			print("True")
		else:
			print("False")
		time.sleep(1.5)
	


if __name__=="__main__": 
	main(1)
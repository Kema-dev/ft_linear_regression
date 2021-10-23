import csv

THETA_LOCATION = '../data/vars.csv'

theta0 = 0
theta1 = 0

class TooManyRows(Exception()):
    """Theta values file has more than 1 row"""
    pass

class TooManyColumns(Exception()):
    """Theta values file has more than 2 columns"""
    pass

def init(new):
	if (new == True):
		try:
			with open(THETA_LOCATION, 'w+') as file:
				file.write('0,0')
		except:
			print('Error during initialization of theta values')
	else:
		try:
			with open(THETA_LOCATION, "r") as file:
				if (file.read() == ""):
					file.close()
					file = open(THETA_LOCATION, "w+")
					file.write('0,0')
					file.close()
					print('File didn t exist, created and initialized it')
					return
				read = csv.reader(file, delimiter = ',')
				if (len(list(read)) > 1):
					raise TooManyRows()
				elif (sum(1 for row in read) > 2):
					raise TooManyColumns()
				else:
					print('file is ok')
		except TooManyColumns:
			print('Theta values file has more than 2 columns')	
		except TooManyRows:
			print('Theta values file has more than 1 row')
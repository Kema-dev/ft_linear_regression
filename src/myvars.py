THETA_LOCATION = '../data/vars.csv'
BACKUP_LOCATION = '../data/vars.csv.backup'

theta0 = 0.0
theta1 = 0.0

class TooManyRows(Exception()):
    """Theta values file has more than 1 row"""
    pass

class WrongNumberComa(Exception()):
    """Theta values file doesn\'t have one and only one coma"""
    pass

def init(new):
	if (new == True):
		try:
			with open(THETA_LOCATION, 'w+') as file:
				file.write('0,0')
				file.close()
				theta0 = 0
				theta1 = 0
				print('Theta file initialized')
				return theta0, theta1
		except:
			print('Error during initialization of theta values')
	else:
		try:
			file = open(THETA_LOCATION, "r")
		except:
			file = open(THETA_LOCATION, "w+")
			file.write('0,0')
			file.close()
			theta0 = 0
			theta1 = 0
			print('File didn\'t exist, created and initialized it')
			return theta0, theta1
			return
		text = file.read()
		try:
			if (text.count(',') != 1):
				raise WrongNumberComa
			elif (text.count('\n') != 0):
				raise TooManyRows
			else:
				val = text.split(',')
				theta0 = float(val[0])
				theta1 = float(val[1])
		except:
			file = open(BACKUP_LOCATION, "w+")
			file.write(text)
			file.close()
			file = open(THETA_LOCATION, "w+")
			file.write('0,0')
			file.close()
			print('File was corrupted, created a new one and initialized it, backed up the corrupted file at ' + BACKUP_LOCATION)
			theta0 = 0
			theta1 = 0
			print('Theta values set to default values, theta0 = ' + str(theta0) + ', theta1 = ' + str(theta1))
			return theta0, theta1
		print('Theta values retrieved, theta0 = ' + str(theta0) + ' $/km, theta1 = ' + str(theta1) + ' $')
		return theta0, theta1
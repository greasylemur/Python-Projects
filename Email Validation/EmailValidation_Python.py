import sys
'py3DNS' in sys.modules
'validate_email' in sys.modules

from validate_email import validate_email 

def EmailTest(eM):
	test = validate_email(eM,verify=True)
	test
	return test

EMT = EmailTest('hcronier@gmail.com')
##Change this email address to test	
	
if  EMT == True: 
	print('Good')
else:
	print('Nope')

	

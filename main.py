import sys

from EuclideanAlgorithm import EuclideanAlgorithm, EuclideanIO
from RSA import RSA_IO

print('The number of system arguments is ' + str(len(sys.argv)))

def mainHelper(userChoice):
	if userChoice == 'e':
		EuclideanIO()
		return 0
	if userChoice == 'r':
		RSA_IO()
		return 0
	else:
		print('Bad Input, please try again')
		return 1

def main():
	if len(sys.argv) == 1:
		choice = 'a'
		while(choice != 'e' and choice != 'r'):
			choice = raw_input('Please enter e for Euclidean Algorithm, or r for RSA: ')
		mainHelper(choice)
	else:
		mainHelper(sys.argv[1])

if __name__ == "__main__": 
    main()

'''
Computes gcd(a, b)
'''

def EuclideanAlgorithm(a, b):
	#continue to divide a by be until remainder is 0
	if a == 0:
		return b
	else:
		return EuclideanAlgorithm(b % a, a)
		
def EuclideanIO():
	print('\nThis program will calculate the greatest common divisor of 2 numbers.')
	a = input('Please enter the first value: ')
	b = input('Please enter the second value: ')

	c = EuclideanAlgorithm(a, b)

	print('The greatest common divisor is ' + str(c))
	
if __name__ == '__main__':
    EuclideanIO()

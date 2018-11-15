def IsSquare(value):
    return value**0.5 == int(value**0.5)
    
def CheckForSquare(N):
	for a in range(1, N):
		b = N + (a ** 2)
		if IsSquare(b):
			return [a, b ** 0.5]
	return [0]
    
def DiffSquares(N):
	result = CheckForSquare(N)
	if result == [0]:
		return [0]
	
	a = result[0]
	print a
	b = result[1]
	print b
	
	p = b - a
	q = a + b
	
	return [p, q]	

def DiffSquaresIO():
	N = input('Please enter the number to factor into 2 primes: ')
	primes = DiffSquares(N)
	
	if primes == [0]:
		print('The number is prime and could not be factored.')
		
	print('The two prime factors of ' + str(N) + ' are: '),
	print primes
	

if __name__ == '__main__':
    DiffSquaresIO()

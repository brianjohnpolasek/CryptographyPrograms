# factorization based on the Trial Division Method
# Link: https://en.wikipedia.org/wiki/Trial_division

def Factor(N):
	currPrime = 2

	finalPrimes = []
	while (N > 1):
		# find a match
		if (N % currPrime == 0):
			finalPrimes.append(currPrime)
			N = N / currPrime

		# check next prime
		else:
			currPrime += 1

	return finalPrimes

def FactorIO():
	N = input('Input the number to factor: ')

	x = Factor(N)

	print('The factored list of primes is: ' + str(x))

if __name__ == '__main__':
    FactorIO()
import sys
sys.path.insert(0, '../CryptoTools')
from EuclideanAlgorithm import EuclideanAlgorithm

def Pollard(a, n):
	print('Test')
	for i in range(1, n):
		a = (a ** i) % n

		gcd = EuclideanAlgorithm(a-1, n)

		#print('gcd: ' + str(gcd))

		if gcd > 1:
			print('iterations: ' + str(i))
			return gcd


def PollardIO():
	a = input('a: ')
	n = input('n: ')

	a = int(a)
	n = int(n)

	#Pollard(a, n)

	gcd = Pollard(a, n)

	p = gcd
	q = n / p

	print('(p, q) = ' + str(p) + ', ' + str(int(q)))
	

if __name__ == '__main__':
    PollardIO()

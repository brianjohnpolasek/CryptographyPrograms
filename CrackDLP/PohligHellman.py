import sys
sys.path.insert(0, '../CryptoTools')
from Factor import Factor
from ChineseRemainderTheorem import ChineseRemainderTheorem

'''
Process:
1. Factor p-1 into small primes Q = q1, .. qi
2. Find Ni = (p - 1) / qi
3. Compute g^(Ni * x) = h^(Ni) mod p
4. Use CRT to find x
'''

def PohligHellman(g, a, p):
	# Factor p-1 into q1, .. qi
	Q = []	# small primes 	
	Q = Factor(p - 1)

	# Find Ni = (p - 1) / qi
	N = []
	for i in range(0, len(Q)):
		N.append((p - 1) / Q[i])

	# Compute g^(Ni * x) = h^(Ni) mod p
	X = []
	for i in range(0, len(Q)):
		X.append(findExp((g ** N[i]) % p, (a ** N[i]) % p, p))

	# Use CRT to find x
	x = ChineseRemainderTheorem(X, Q)

	return x

def findExp(g, a, p):
	# find the exponent of the smaller DLP
	for i in range(0, p):
		if ((g ** i) % p == a):
			return i

	return None
		

def PohligHellmanIO():
	g = input('g: ')
	a = input('a: ')
	p = input('p: ')

	x = PohligHellman(g, a, p)

	print('The value of x is: ' + str(x))

if __name__ == '__main__':
    PohligHellmanIO()
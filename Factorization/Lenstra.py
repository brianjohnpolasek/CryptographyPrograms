import random
import math
import sys
sys.path.insert(0, '../CryptoTools')
from EuclideanAlgorithm import EuclideanAlgorithm
from ExtendedEuclidean import ExtendedEuclid
from ModInverse import ModInv

'''
Process:
Input E over field N where E is y^2 = x^3 + A*x + B and P is point on E
1. determine if P is on E
2. Like pollard, compute 2P, 3P = 2P + P, 4P = 2P + 2P ...
3. If gcd(N, [n]*P) >= 1, return the result as p
4. q = N / p
'''

# determines slope for use in "pointAddition"
def computeLambda(E, P, Q, N):
	# initialize lambda
	m = 0

	if P == Q:
		num = (3 * P[0] ** 2 + E[0]) % N
		den = (2 * P[1]) % N

		#m = (num * ModInv(den, N)) % N	#too slow, use Extended Euclidean instead
		#m = (num * ExtendedEuclid(den, N)) % N
		gcd = ExtendedEuclid(den, N)
		m = (num * gcd[0]) % N

	else:
		num = (Q[0] - P[0]) % N
		den = (Q[1] - P[1]) % N

		m = (num * ModInv(den, N)) % N	

	return m

# computes point addition on a specified E-curve in "pointLoop"
def pointAddition(E, P, Q, N):
	R = []
	m = computeLambda(E, P, Q, N)

	x3 = ((m ** 2) - P[0] - Q[0]) % N
	R.append(x3)

	y3 = ((m * (P[0] - x3)) - P[1]) % N
	R.append(y3)

	return R

# checks for solutions through continuous multiplication of points on the
def pointLoop(E, P, N):
	Q = P
	for i in range(0, 20):	# hardcoded limit to increase performance
		Q = pointAddition(E, P, Q, N)

		d = EuclideanAlgorithm(N, 2*P[1])

		if d >= 2:
			return d

		P = Q
	return -1.0

# runs Lenstra's on a specified point and E-curve
def Lenstra(E, P, N):
	d = pointLoop(E, P, N)	

	return d

# runs Lenstra's with a random point and on a random E-curve
def Lenstra(N):
	sqrtN = int(math.sqrt(N))
	for i in range(0, sqrtN):
		# choose a random E-curve and point on the curve
		x = random.randint(1, sqrtN)
		y = random.randint(1, sqrtN)
		a = random.randint(1, sqrtN)	
		b = ((y ** 2) - (x ** 3) - (a * x)) % sqrtN

		P = [x, y]
		E = [a, b]
		print("Using point " + str(P) + " on the Elliptical Curve " + str(E))

		p = pointLoop(E, P, N)

		if isinstance(p, int):
			return p

	return -1

# prompts user if no number specified through the command line
def LenstraIO():
	# for y^2 = x^3 + Ax + B. E[0] = A, E[1] = B
	E = []

	# for P = (x, y), P[0] = x, p[1] = y3
	P = []

	N = int(input("Enter number to factor: "))
	#N = int(N)

	p = Lenstra(N)

	printSolution(p, N)

def printSolution(p, N):
	# check if solution is possible
	if p > 0:
		q = int(N / p)
		print("A factorization of " + str(N) + " is " + str(q) + " and " + str(p))
	else:
		print("The number " + str(N) + " is not factorable.")


if __name__ == '__main__':
	print('---------------------------------')
	print('Lenstra\'s Factorization Algorithm')
	print('---------------------------------')

	if len(sys.argv) > 1:
		N = int(sys.argv[1])
		p = Lenstra(N)
		printSolution(p, N)
	else:
		LenstraIO()
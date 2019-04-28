import sys
sys.path.insert(0, '../CryptoTools')
from EuclideanAlgorithm import EuclideanAlgorithm

# Input E over field N where E is y^2 = x^3 + A*x + B and P is point on E
# 1. determine if P is on E
# 2. Like pollard, compute 2P, 3P = 2P + P, 4P = 2P + 2P ...
# 3. If gcd(N, [n]*P) >= 1, return the result ad p
# 4. q = N / p

def computeLambda(E, P, Q, N):
	# initialize lambda
	m = 0

	if P == Q:
		num = (3 * P[0] ** 2 + E[0]) % N
		den = (2 * P[1]) % N

		m = (num * ModInv(den, N)) % N

	else:
		num = (Q[0] - P[0]) % N
		den = (Q[1] - P[1]) % N

		m = (num * ModInv(den, N)) % N		

	return m

def pointAddition(E, P, Q, N):
	R = []
	m = computeLambda(E, P, Q, N)

	x3 = ((m ** 2) - P[0] - Q[0]) % N
	R.append(x3)

	y3 = ((m * (P[0] - x3)) - P[1]) % N
	R.append(y3)

	return R

def pointLoop(E, P, Q, N):
	Q = P
	for i in range(0, N):
		Q = pointAddition(E, P, Q, N)

		d = EuclideanAlgorithm(N, 2*P[1])

		if d >= 2:
			return d

		P = Q

def Lentra(E, P, N):
	d = pointLoop(Em P, N)	

	return d

		

def LentraIO():
	print('---------------------------------')
	print('Lentra\'s Factorization algorithm')
	print('---------------------------------')

	# for y^2 = x^3 + Ax + B. E[0] = A, E[1] = B
	E = []

	# for P = (x, y), P[0] = x, p[1] = y3
	P = []


if __name__ == '__main__':
    LentraIO()
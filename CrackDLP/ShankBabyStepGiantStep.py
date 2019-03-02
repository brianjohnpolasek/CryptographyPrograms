import math
import sys
sys.path.insert(0, '../CryptoTools')

from ModInverse import ModInv

def Shank(g, a, N):
	# calculate index number
	n = int(1 + math.floor( math.sqrt(N) ))

	# baby step section
	babyStep = dict()

	for i in range(0, N - 1):
		babyStep[(g ** i) % N] = i

	# giant step section
	a_inv = ModInv(a ** n, N)

	giantStep = a

	for j in range(0, n - 1):
		if (giantStep in babyStep):
			return ((j * n) + babyStep[giantStep]) % N
		else:
			giantStep = (giantStep * a_inv) % N

	# otherwise no solution
	return None		

def ShankIO():
	g = input('g: ')
	a = input('a: ')
	N = input('N: ')

	x = Shank(g, a, N)

	print('The value of x is: ' + str(x))

if __name__ == '__main__':
    ShankIO()

'''
Process:
1. let n = 1 + floor( sqrt(N) )
'''
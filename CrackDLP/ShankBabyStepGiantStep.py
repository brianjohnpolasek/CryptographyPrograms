import math
import sys
sys.path.insert(0, '../CryptoTools')

from ModInverse import ModInv

'''
Process:
1. let n = 1 + floor( sqrt(N) )
2. Generate Baby List: {1, g^1, g^2, ... g^n}
3. Generate Giant List: {a, a * g^-n, a* g^-2n, ... a * g^-n^2}
4. find a match between the two lists
5. The result for a match "g^i = a * g^-j*n" will be "x = j*n + i"
'''

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
	g = int(input('g: '))
	a = int(input('a: '))
	N = int(input('N: '))

	x = Shank(g, a, N)

	print('The value of x is: ' + str(x))

if __name__ == '__main__':
	print('-------------------------------------')
	print('Shank\s Baby Step Giant Step Algorithm')
	print('-------------------------------------')

	if len(sys.argv) > 3:
		g = int(sys.argv[1])
		a = int(sys.argv[2])
		N = int(sys.argv[3])

		x = Shank(g, a, N)

		print('The value of x is: ' + str(x))	

	else:
		ShankIO()


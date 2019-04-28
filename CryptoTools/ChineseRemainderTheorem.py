import re
from ModInverse import ModInv

'''
Example Input:
x = c1 mod n1
x = c2 mod n2
x = c3 mod n3
...
x = cj mod nj

Example Output:
y = (c1 * n1 * n1^-1) + ... + (cj * nj * nj^-1) mod (n1 * ... * nj)
'''

def ChineseRemainderTheorem(C, N):
	print('Input:\n' + 'C = ' + str(C) + '\nN = ' + str(N) + '\n')
	numItems = len(C)

	invN = []
	othN = []
	totN = 1
	for i in range(0, numItems):
		# keep running multiplicative total of modulos
		totN = totN * N[i]

	for i in range(0, numItems):
		# calculate the modular inverses for each modulo

		othN.append(totN / N[i])

		invN.append(ModInv(othN[i], N[i]))
	
	# compute addition of (cj * nj * nj^-1)
	y = 0
	for i in range(0, numItems):
		y = y + (C[i] * invN[i] * othN[i])

	# find y mod the multiplication of all of the modulos
	y = y % totN

	return y
	
def ChineseRemainderTheoremIO():
	# initialize congruences and mods	
	inC = ''
	inN = ''
	outC = []
	outN = []


	inC = int(input('Please enter the known congruences, seperated by spaces: '))

	matchC = re.findall('[^ ]+', str(inC))

	inN = int(input('Please enter the modulos, separated by spcases:'))

	matchN = re.findall('[^ ]+', inN)

	if (len(matchC) != len(matchN)):
		print('Congruences and modulos must have the same length.')
		exit()

	for i in range(0, len(matchC)):
		outC.append(int(matchC[i]))
		outN.append(int(matchN[i]))

	x = ChineseRemainderTheorem(outC, outN)

	print('The value of x is: ' + str(x))

if __name__ == '__main__':
	print('-----------------------------------')
	print('Chinese Remainder Theorem Algorithm')
	print('-----------------------------------')

	if len(sys.argv) > 2:
		C = int(sys.argv[1])
		N = int(sys.argv[2])
		x = ChineseRemainderTheorem(C, N)

		print('The value of x is: ' + str(x))

		printSolution(p, N)
	else:
		ChineseRemainderTheoremIO()
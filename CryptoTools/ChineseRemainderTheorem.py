import re
from ModInverse import ModInv
#from EuclideanAlgorithm import EuclideanAlgorithm

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
		#Ni = multHelper(i, N)

		othN.append(totN / N[i])

		invN.append(ModInv(othN[i], N[i]))
	
	# compute addition of (cj * nj * nj^-1)
	y = 0
	for i in range(0, numItems):
		y = y + (C[i] * invN[i] * othN[i])

	# find y mod the multiplication of all of the modulos
	#y = EuclideanAlgorithm(y, totN)
	y = y % totN

	return y

# calculates the multiplication of everything except the value passed in
'''
def multHelper(i, N):
	N1 = list(N)
	N1.pop(i)
	Ni = 1
	for j in range(0, len(N1)):
		Ni = Ni * N1[j]

	return Ni
'''
	
def ChineseRemainderTheoremIO():
	# initialize congruences and mods	
	inC = ''
	inN = ''
	outC = []
	outN = []


	inC = raw_input('Please enter the known congruences, seperated by spaces: ')

	matchC = re.findall('[^ ]+', str(inC))

	inN = raw_input('Please enter the modulos, separated by spcases:')

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
    ChineseRemainderTheoremIO()

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
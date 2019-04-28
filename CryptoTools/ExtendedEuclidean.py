import sys

def ExtendedEuclid(a, M) : 
	if a == 0:
		return (M, 0, 1)
	else:
		gcd, x, y = ExtendedEuclid(M % a, a)
		return (gcd, y - (M / a) * x, x)

def ExtendedEuclidIO():
	a = int(input("Enter the value you want the modular inverse of: "))
	M = int(input("Enter the value of the modulo: "))

	result = ExtendedEuclid(a, M)

	printResult(result, M)

def printResult(result, M):
	if isinstance(result, int):
		print("The modular Inverse is " + str(result))
	else:
		print("There is no modulare inverse for " + str(a) + " mod " + str(M))

if __name__ == '__main__':
	print('----------------------------')
	print('Extended Euclidean Algorithm')
	print('----------------------------')

	if len(sys.argv) > 1:
		a = sys.argv[1]
		M = sys.argv[2]
		result = ExtendedEuclid(a, M)

		printResult(result[0], M)
	else:
		ExtendedEuclidIO()
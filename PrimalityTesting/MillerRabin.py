import sys
sys.path.insert(0, '../CryptoTools')
from EuclideanAlgorithm import EuclideanAlgorithm
from FastPoweringAlgorithm import FastPower

def gcd(a,b):
	if (b == 0):
		return a
	else:
		return gcd(b, a % b)

def MillerRabin(n):
	if (n % 2 == 0):
		print(n ++ " is Composite")

	# find d where n-1 = 2^r * d
	k = 0
	q = n - 1
	while q % 2 == 0:
		q /= 2
		k = k + 1

	print("k: " + str(k))
	print("q: " + str(q))


	# find a where gcd(a, n) == 1
	a = 0
	for i in range(2, n):
		a = i 
		if EuclideanAlgorithm(a, n) == 1:
			break
	
	print("a: " + str(a))

	a = FastPower(a, q, n)

	print("a: " + str(a))

	if a == 1:
		print("Test failed")

	for i in range(0, k-1):
		a = FastPower(a, i, n)
		if a == -1:
			print("Test failed")

	print(str(n) + " is Composite")

def MillerRabinIO():
	print("-------------------------------")
	print("Miller-Rabin Test for Primality")
	print("-------------------------------")
	n = input("Please enter an integer larger than two that you would like to test for primality: ")

	n = int(n)

	if (n <= 2):
		print("The number must be larger than 2")

	MillerRabin(n)
	
if __name__ == '__main__':
    MillerRabinIO()

'''
// It returns false if n is composite and returns true if n
// is probably prime.  k is an input parameter that determines
// accuracy level. Higher value of k indicates more accuracy.
bool isPrime(int n, int k)
1) Handle base cases for n < 3
2) If n is even, return false.
3) Find an odd number d such that n-1 can be written as d*2^r. 
   Note that since n is odd, (n-1) must be even and r must be 
   greater than 0.
4) Do following k times
     if (millerTest(n, d) == false)
          return false
5) Return true.

// This function is called for all k trials. It returns 
// false if n is composite and returns false if n is probably
// prime.  
// d is an odd number such that  d*2r = n-1 for some r >= 1
bool millerTest(int n, int d)
1) Pick a random number 'a' in range [2, n-2]
2) Compute: x = pow(a, d) % n
3) If x == 1 or x == n-1, return true.

// Below loop mainly runs 'r-1' times.
4) Do following while d doesn't become n-1.
     a) x = (x*x) % n.
     b) If (x == 1) return false.
     c) If (x == n-1) return true.
'''

def gcd(a,b):
	if (b == 0):
		return a
	else:
		return gcd(b, a % b)

print("Miller-Rabin Test for Primality")
testNum = input("Please enter an integer larger than two that you would like to test for primality: ")

if (testNum % 2 == 0):
	print("The number must be larger than 2")

if (testNum % 2 == 0):
	print(testNum ++ " is Composite")
	

	
#set a = a^q % testNum

#if a congruent to 1, return test failed

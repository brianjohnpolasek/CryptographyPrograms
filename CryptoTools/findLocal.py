def findLocal(g, a, p):
	for i in range(0, p):
		if (((g ** i) % p) == a):
			print('Value of x: ' + i)
	print('No such solution')

def findLocalIO():
	g = input('g: ')
	a = input('a: ')
	p = input('p: ')

	findLocal(g, a, p)


if __name__ == '__main__':
    findLocalIO()
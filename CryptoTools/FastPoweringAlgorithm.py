def FastPower(base, exp, mod):
	result = 1
	
	while exp > 0:
		if exp % 2 == 1: # odd number
			result = (base * result) % mod
		
		# even number
			base = (base ** 2) % mod
			exp = exp / 2
		
	return result
	
def FastPowerIO():
	print('\nWelcome to the fast powering algorithm!')
	print('Please enter the following:')
	base = input('Base value: ')
	exp = input('Power value: ')
	mod = input('Mod value: ')

	answer = FastPower(int(base), int(exp), int(mod))
	
	print('The solution is: ' + str(answer))
	
if __name__ == '__main__':
    FastPowerIO()

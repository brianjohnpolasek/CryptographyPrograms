def ModInv(value, mod):
	value = value % mod
	for i in range(1, mod):
		if ((value * i) % mod == 1):
			return i
	return 1
			
if __name__ == '__main__':
	value = input('Enter the value: ')
	mod = input('Enter the mod: ')
	print('The modular inverse is: ' + str(ModInv(value, mod)))

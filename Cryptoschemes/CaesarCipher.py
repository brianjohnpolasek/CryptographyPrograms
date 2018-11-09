import sys
sys.path.insert(0, '../CryptoTools')
from StringNumberConverter import StrToNum, NumToStr

def Encrypt(plaintext, shamt):
	if shamt > 26:
		raise Exception('The shift amount should not exceed 26. The value of x was: {}'.format(shamt))
	
	ciphertext = []
	convert = StrToNum(plaintext)
	
	for c in convert:
		c = (c + shamt) % 26
		ciphertext.append(c)
	
	return NumToStr(ciphertext)
	
def Decrypt(ciphertext, shamt):
	if shamt > 26:
		raise Exception('The shift amount should not exceed 26. The value of x was: {}'.format(shamt))
	
	plaintext = []
	convert = StrToNum(ciphertext)

	for c in convert:
		c = (c - shamt) % 26
		plaintext.append(c)
	
	return NumToStr(plaintext)
		
def CaesarCipherIO():
	print('Welcome to the simple Caesarcipher calculator!')
	userInput = -1
	while userInput != 1 and userInput != 2:
		userInput = input('Enter 1 to encrypt and 2 to decrypt: ')

	shamt = input('Please enter the shift amount: ')
		
	if userInput == 1:	
		plain = raw_input('Please enter the plaintext: ')
		cipher = Encrypt(plain, shamt)
	
		print ('The encoded message is: ' + cipher)
		
	if userInput == 2:
		cipher = raw_input('Please enter the ciphertext: ')
		plain = Decrypt(cipher, shamt)
		
		print ('The original message is: ' + str(plain))
	
	
if __name__ == '__main__':
    CaesarCipherIO()

import sys
sys.path.insert(0, '../CryptoTools')
from FastPoweringAlgorithm import FastPower
from ModInverse import ModInv
from StringNumberConverter import StrToNum, NumToStr
#~ from EuclideanAlgorithm import EuclideanAlgorithm

import random

def GetPrivateKey(prime):
	private_key = -1
	while private_key < 0:
		private_key = input('Please enter your positive private key: ')
		private_key = private_key % prime
		
	return private_key
		
def GetPlaintext():
	message = raw_input('Please enter your plaintext (Ex. The cow says moo.): ')
	plaintext = StrToNum(message)
	print('Your plaintext is ' + str(plaintext))
	
	return plaintext

def ComputePublicKey(prime, prim_root):
	private_key = GetPrivateKey(prime)
	public_key = FastPower(prim_root, private_key, prime)
	
	return public_key

def EncryptMessage(public_key, prime, prim_root, plaintext):
	rand_exp = random.randint(0, prime - 1)
	cipher_1 = (prim_root ** rand_exp) % prime
	
	cipher_2 = []
	for p in plaintext:
		print p,
		temp = (p * (public_key ** rand_exp)) % prime
		cipher_2.append(temp)
	
	return [cipher_1, cipher_2]
	
def DecryptCipher(cipher, prime):
	private_key = GetPrivateKey(prime)
	c1 = cipher[0]
	c2 = cipher[1]
	
	x = (c1 ** private_key) % prime
	x_inv = ModInv(x, prime)
	
	print ('x inverse: ' + str(x_inv))
	
	plaintext = []
	for c in c2:
		temp = (x_inv * c) % prime
		plaintext.append(temp)
	
	message = NumToStr(plaintext)
	
	return message
	

def ElGamalIO():
	print('\n')	#give some space
	print('Demonstration of the El Gamal Cryptoscheme')
	print('Note: When encrypting strings, the prime modulus must be greater than 26')
	
	print('\n')
	
	prime = input('Please select a large, positive prime number: ')
	print('Your prime is ' + str(prime))
	prim_root = input('Please enter a primitive root (preferably with high order): ')
	print('Your primitive root is ' + str(prim_root))
	
	print('\n')
	
	print('We will now generate a public key:')
	print('(Note, make sure you remember your private key which will be used later)')
	public_key = ComputePublicKey(prime, prim_root)
	print('The public key is ' + str(public_key))
	
	print('\n')
	
	print('Next, a message will be encrypted using the public key')
	plaintext = GetPlaintext()
	cipher = EncryptMessage(public_key, prime, prim_root, plaintext)
	#~ print('The cipher keys are ' cipher[0] + ' and ' + cipher[1])
	print('The cipher keys are '),
	print cipher[0],
	print(' and '),
	print cipher[1]
	
	print('\n')
	
	print('Now we will decrypt the message:')
	message = DecryptCipher(cipher, prime)
	print('The original message is ' + message)

if __name__ == '__main__':
    ElGamalIO()

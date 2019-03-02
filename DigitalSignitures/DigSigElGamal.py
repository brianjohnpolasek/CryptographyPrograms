import sys
sys.path.insert(0, '../CryptoTools')
from FastPoweringAlgorithm import FastPower
from ModInverse import ModInv
from StringNumberConverter import StrToNum, NumToStr
from EuclideanAlgorithm import EuclideanAlgorithm

import random

def GetPrivateKey(prime):
	private_key = -1
	while private_key < 0:
		private_key = input('Please enter your positive private key: ')
		private_key = private_key % prime
		
	return private_key
		
def GetRandVal(prime):
	rand_val = random.randint(0, prime - 1)
	while EuclideanAlgorithm(rand_val, prime - 1) != 1:
		print('Random Value: ' + str(rand_val))
		rand_val = (rand_val + 1) % (prime - 1)
		
	return rand_val
		
def GetDocument():
	document = input('Please enter your document: ')
	
	return document

def ComputePublicKey(prime, prim_root):
	private_key = GetPrivateKey(prime)
	public_key = FastPower(prim_root, private_key, prime)
	
	return public_key

def EncryptDocument(public_key, prime, prim_root, document):
	rand_val = GetRandVal(prime)
	cipher_1 = (prim_root ** rand_val) % prime
	
	
	print('We need the private key to generate the ciphertext.')
	private_key = GetPrivateKey(prime)
	
	cipher_2 = ((document - (private_key * cipher_1)) * ModInv(rand_val, prime)) % (prime - 1)
	
	return [cipher_1, cipher_2]
	
def VerifyDocument(cipher, prime, public_key, prim_root, document):
	private_key = GetPrivateKey(prime)
	c1 = cipher[0]
	c2 = cipher[1]
	
	lhs = ((public_key ** c1) * (c1 ** c2)) % prime
	print('Left Hand Side: ' + str(lhs))
	rhs = (prim_root ** document) % prime
	print('Right Hand Side: ' + str(rhs))
	
	return [lhs, rhs]
	

def ElGamalDigSigIO():
	print('\n')	#give some space
	print('Demonstration of the El Gamal Digital Signiture Algorithm')
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
	document = GetDocument()
	cipher = EncryptDocument(public_key, prime, prim_root, document)
	#~ print('The cipher keys are ' cipher[0] + ' and ' + cipher[1])
	print('The cipher keys are '),
	print cipher[0],
	print(' and '),
	print cipher[1]
	
	print('\n')
	
	print('Now we will decrypt the message:')
	result = VerifyDocument(cipher, prime, public_key, prim_root, document)

if __name__ == '__main__':
    ElGamalDigSigIO()

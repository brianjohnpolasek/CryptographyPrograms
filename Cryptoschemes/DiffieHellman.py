#Diffie Helman Key Exchange

import sys
sys.path.insert(0, '../CryptoTools')
from StringNumberConverter import StrToNum, NumToStr
from FastPower import FastPower
from ModInverse import ModInv

import threading, Queue, random

def Setup(base, exp, mod):
	if exp < 0:
		exp = random.randint(2, mod - 1)
		
	result = FastPower(base, exp, mod)
		
	return result
	
def ComputeKey(public_key, private_key, mod):
	return FastPower(public_key, private_key, mod)
	
def Encrypt(plaintext, secret_key, mod):
	ciphertext = []
	convert = StrToNum(plaintext)
	
	for c in convert:
		c = (c * secret_key) % mod
		ciphertext.append(c)
	
	return NumToStr(ciphertext)

def Decrypt(ciphertext, secret_key, mod):
	plaintext = []
	convert = StrToNum(ciphertext)
	
	inverse = ModInv(secret_key, mod)

	for c in convert:
		c = (c * inverse) % mod
		plaintext.append(c)
	
	return NumToStr(plaintext)
	
def Alice(q):
	prime = input('Please enter a large prime: ')
	q.put(prime)
	prim_root = input('Please enter a primitive root of the prime: ')
	q.put(prim_root)
	
	private_key = input('Please enter your private key (1-prime): ')
	
	public_key = Setup(prim_root, private_key, prime)
	print('Your public key is: ' + str(public_key))
	
	print('Sending you public key to Bob...'
	q.put(public_key)
	
	print('Recieving public key from Bob...')
	bob_public_key = q.get()
	
	secret_key = ComputeKey(bob_public_key, private_key, prime)
	print('The secret key is: ' + str(secret_key))
	
	userInput = raw_input('Would you like to send a message to Bob? (y/n): ')
	 
	if userInput == 'y':
		q.put('y')
		message = raw_input('What message would you like to send? ')
		q.put(Encrypt(message, secret_key)
		bob_response = q.get()
		
		print('Bob says your message was: ' + bob_response)
	else:
		q.put('n')
		print('Thank you for using this program!')
	
def Bob(q):
	print('Waiting for a prime from Alice...')
	prime = q.get()
	print('Recieved ' + str(prime)	+ ' from Alice')
	
	print('Waiting for a primitive root from Alice...')
	prim_root = q.get()
	print('Recieved ' + str(prim_root)	+ ' from Alice')
	
	print('Recieving public key from Alice...')
	alice_public_key = q.get()
	print('Recieved ' + str(alice_public_key) + ' from Alice')
	
	print('Calculating public key')
	public_key = Setup(prim_root, -1, prime)
	print('Public Key is: ' + str(public_key))
	
	print('Sending public key to Alice...')
	q.put(public_key)
	
	secret_key = ComputeKey(alice_public_key, private_key, prime)
	print('The secret key generated is: ' + str(secret_key))
	
	userInput = q.get()
	
	if userInput == 'y':
		ciphertext = q.get()
		q.put(Decrypt(ciphertext, secret_key)
		
	print('Exiting')
	
	

def DiffieHellmanIO():
	print('Welcome to the Diffie-Hellamn Key Exchange!)
	
	q = Queue.Queue()
	thread1 = threading.Thread(Alice, q)
	thread1 = threading.Thread(Bob, q)
	
	thread1.start()
	thread2.start()

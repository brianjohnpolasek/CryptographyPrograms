# to generate random integer values
from random import seed
from random import randint

from EuclideanAlgorithm import EuclideanAlgorithm



def RSA_IO():
	print('\nThis program will demonstrate how RSA encryption works.')
	#select 2 primes and compute n = p*q
	p = input('Please enter a large prime: ')
	q = input('Please enter another large prime: ')

	n = p * q
	print('The value for n is ' + str(n))

	#compute phi(n) = (p-1)(q-1)
	phi_n = (p - 1)*(q - 1)
	print('The value for Phi(n) is ' + str(phi_n))

	#choose 2 < e < phi(n) for the encryption value
	e = 1
	print('Please enter a value for encryption larger than 1 and less than ' + str(phi_n))
	while e < 2:
		e = input('Make sure the value is coprime to ' + str(phi_n) + ': ')
		if e > phi_n:
			e = e % phi_n
		if EuclideanAlgorithm(e, phi_n) != 1:
			e = 1

	#choose random number 1 < k < n
	#k = randint(1, n)
	k = -1
	while k < 1 and k > n:
		k = input('Please enter a random value for k greater than 2 but less than ' + str(n) + ': ')

	#calculate decryption value
	d = (((k * phi_n) + 1) / e) % n
	print('The value for decryption is ' + str(d))

	m = input('Please enter the message you would like to send: ')
	
	if type(m) == 'str':
		print('Needs to be an integer')

	#encryption
	c = (m**e) % n
	print('Your encrypted cyphertext is ' + str(c))

	#decription:
	m1 = (c**d) % n
	print('Your decrypted message is ' + str(m1))

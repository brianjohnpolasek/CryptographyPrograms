def shift(plaintext, shamt):
	if shamt > 26:
		raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
	#endif
	
	cyphertext = plaintext
	
	for c in cyphertext:
		c = c + shamt
	#endfor
	
	return cyphertext
		
def main():
	result = shift("Hello", 4)
	print(result)

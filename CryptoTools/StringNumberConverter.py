def StrToNum(string):
	numbers = []
	temp = 0
	for s in string:
		#~ print ord(s) # for testing
		if 65 <= ord(s) <= 90:
			temp = ord(s) - 65
			numbers.append(temp)
		if 97 <= ord(s) <= 122:
			temp = ord(s) - 97
			numbers.append(temp)
		else:
			print (str(s) + ' was ignored or converted.')
			pass
		
		
			
	return numbers
	
def NumToStr(numbers):
	string = ""
	for n in numbers:
		n = n + 97
		string = string + chr(n)
		
	return string
		
	
def ConverterIO():
	userInput = -1
	while userInput < 1 or userInput > 2:
		userInput = input('Type 1 for String to number, and 2 for number to string: ')
		if userInput == 1:
			string = ""
			numbers = []
			string = raw_input('Please type in the string to convert: ')
			numbers = StrToNum(string)
			print('The resulting numbers are: ')
			
			for e in numbers:
				print str(e)
				
		if userInput == 2:
			numbers = []
			numbers = input('Please enter the numbers as a list. Ex [1,2,3]: ')
			result = NumToStr(numbers)
			
			print('The resulting string is: ' + result)
			
		else:
			print ('Please try again')

if __name__ == '__main__':
    ConverterIO()

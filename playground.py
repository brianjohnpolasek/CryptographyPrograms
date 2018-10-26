name = raw_input("Give me your name: ")
print("Your name is " + name)

default = 'Brian'

if default == name:
	print('The names match')
else:
	print('No match')

temp = 'a'
while temp != 'b':
	temp = raw_input('Please enter the letter b: ')

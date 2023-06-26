def convert_to_int(string):
	'''Takes in a string and returns its integer representation.'''
	print(list(string.encode('ascii')))

string = input('Enter a string: ')
convert_to_int(string)
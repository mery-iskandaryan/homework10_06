def find_last_not_of(string, char_seq):
	'''Takes in a string and a character sequence. Returns the 
	last character equal to none of the characters in the given
	character sequence.'''
	rev = string[::-1]
	for i in rev:
		if i not in char_seq:
			print(i)
			break	

string = input('Enter a string: ')
char_seq = input('Enter a character sequence: ')
find_last_not_of(string, char_seq)
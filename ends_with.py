def ends_with(first_string, second_string):
	'''Takes in two strings, returns 'True' if the first string
	ends with the second one'''
	len_second = len(second_string)
	if first_string[-len_second:] == second_string:
		print('True')
	else:
		print('The first string does not end with the second one')

first = input('Enter the first string: ')
second = input('Enter the second string: ')
ends_with(first, second) 
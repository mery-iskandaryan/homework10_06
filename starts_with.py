def starts_with(first_string, second_string):
	'''Takes in 2 strings, returns 'True' if the first string				
	starts with the second one'''
	len_second = len(second_string)
	if first_string[:len_second]  == second_string:
		print('True')
	else:
		print("The first string doesn't start with the second one")


first = input('Enter the first string: ')
second = input('Enter the second string: ')
starts_with(first, second)
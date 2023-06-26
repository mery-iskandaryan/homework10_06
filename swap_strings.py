def swap_strings(first_string, second_string):
	'''Takes in two strings and swaps their values'''
	intermediate_str = first_string
	first_string = second_string
	second_string = intermediate_str 
	print( first_string, second_string)


first = input('Enter the first string: ')
second = input('Enter the second string: ')
swap_strings(first, second)
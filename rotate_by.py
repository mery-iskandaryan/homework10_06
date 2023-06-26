def rotate_by(arr, num):
	'''Takes in integer array and a number. Returns the array rotated
	by the specified number of positions (given by the second argument).'''
	for i in range(num):	
		arr.append(arr[i])
	arr = arr[num:]
	print(arr)



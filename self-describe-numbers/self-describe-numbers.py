with open('test_file.txt') as test_file:
	for line in test_file:
		is_self_descibing = True
		numbers = line.strip()
		for index, number in enumerate(numbers):
			if numbers.count(str(index)) == int(number):
				is_self_descibing = is_self_descibing & True
			else:
				is_self_descibing = is_self_descibing & False
		print '1' if is_self_descibing else '0'
with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		for char in line:
			if line.count(char) == 1:
				print char
				break
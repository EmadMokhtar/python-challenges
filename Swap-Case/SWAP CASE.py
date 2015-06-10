with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		print line.swapcase().strip()
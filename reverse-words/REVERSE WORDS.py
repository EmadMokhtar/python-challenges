with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		if line:
			print ' '.join(item for item in reversed(line.split()))
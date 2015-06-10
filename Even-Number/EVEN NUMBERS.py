with open('test_files.txt') as test_file:
	for line in test_file:
		if int(line) % 2 == 0:
			print 1
		else:
			print 0
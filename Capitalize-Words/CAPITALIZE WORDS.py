with open('test_file.txt') as test_file:
	for line in test_file:
		print " ".join([item[0].upper() + item[1:] for item in line.strip().split()])
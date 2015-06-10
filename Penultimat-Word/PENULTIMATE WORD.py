with open('test_files.txt') as test_file:
	for line in test_file:
		words = line.strip().split()
		print words[len(words) - 2]
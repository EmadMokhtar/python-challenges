with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		words = (word for word in line.strip().split())
		print max(words, key=lambda x:len(x))
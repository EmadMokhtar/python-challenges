with open('test_file.txt','r') as test_file:
	for line in test_file:
		words = line.rstrip().split()
		swapped_numbers_words = []
		for word in words:
			if word[0] != word[len(word)-1]:
				swapped_numbers_words.append(word[len(word)-1] + word[1:len(word)-1] + word[0])

		print ' '.join(swapped_numbers_words)
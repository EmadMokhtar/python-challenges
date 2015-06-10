with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		writer_name = []
		encyrpted_text, keys = line.rstrip().split('|')
		keys = [int(i) for i in keys.split()]
		for key in keys:
			writer_name.append(encyrpted_text[key-1])
		print ''.join(writer_name)
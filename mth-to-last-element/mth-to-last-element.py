with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		line = line.rstrip().split()[::-1]
		element_list = line[1:]
		index = int(line[0])
		try: 
			print element_list[index-1]
		except IndexError:
			print ''
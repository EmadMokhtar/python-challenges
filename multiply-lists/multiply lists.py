with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		results = []
		first_list, second_list = [l.split() for l in line.rstrip().split(' | ')]
		for first_value, second_value in zip(first_list, second_list):
			first_value = int(first_value)
			second_value = int(second_value)
			results.append(first_value * second_value)

		print ' '.join([str(r) for r in results])

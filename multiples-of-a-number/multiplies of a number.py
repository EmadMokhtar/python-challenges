with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		x, n = [int(number) for number in line.strip().split(',')]
		attmpets = 1
		multiplication = n * attmpets
		while multiplication <= x:
			attmpets += 1
			multiplication = n * attmpets
		print multiplication
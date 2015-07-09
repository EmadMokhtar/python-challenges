def get_lowest_number_index(lowest_number, numbers):
	if lowest_number == 0:
		return lowest_number

	numbers = numbers.replace(' ', '').rstrip()
	return numbers.index(str(lowest_number))+1

with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		numbers = set((int(n),line.rstrip().split().count(n)) for n in line.rstrip().split())
		numbers = sorted(numbers, key=lambda x: x[0])
		lowest_number = 0
		for number in numbers:
			if number[1] == 1:
				lowest_number = number[0]
				break

		print get_lowest_number_index(lowest_number, line)
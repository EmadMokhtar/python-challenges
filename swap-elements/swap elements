with open('test_file.txt','r') as test_file:
	for line in test_file:
		number_list, swap_indexs = line.rstrip().split(' : ')
		number_list = [n for n in number_list.split()]
		swap_indexs = [s for s in swap_indexs.split(', ')]
		for index in swap_indexs:
			index1, index2 = [int(i) for i in index.split('-')]
			number_list[index2], number_list[index1] = number_list[index1], number_list[index2]

		print ' '.join(number_list)
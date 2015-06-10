def find_unique_elements(list_of_elements):
	unique_elements = []
	for element in list_of_elements:
		if element not in unique_elements:
			unique_elements.append(element)

	return sorted(unique_elements)


with open('test_file.txt') as test_file:
	for line in test_file:
		list_of_elements = [int(l) for l in set(line.strip().split(','))]
		print ','.join(str(l) for l in sorted(list_of_elements))
def are_equal(binary,position1,position2):
	result = bin(binary)[-position1] == bin(binary)[-position2]
	print str(result).lower()

with open('test_file.txt','r') as test_file:
	for line in test_file:
		binary, position1, position2 = [int(item) for item in line.strip().split(',')]
		are_equal(binary, position1, position2)
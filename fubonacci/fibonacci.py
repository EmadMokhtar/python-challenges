def fibonacci(number):
	if number == 1 or number == 0:
		return number

	return fibonacci(number-1) + fibonacci(number-2)

with open('test_file.txt') as text_file:
	for line in text_file:
		number = int(line.strip()) #Remove the any tailing spaces and new line characters
		print fibonacci(number)
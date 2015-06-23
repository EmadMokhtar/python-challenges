text_to_numbers = {
	'zero':'0',
	'one':'1',
	'two':'2',
	'three':'3',
	'four':'4',
	'five':'5',
	'six':'6',
	'seven':'7',
	'eight':'8',
	'nine':'9'
}

with open('test_file.txt') as test_file:
	for line in test_file:
		numbers_as_text = line.strip().split(';')
		numbers = ''
		for num in numbers_as_text:
			numbers += text_to_numbers[num]
		print numbers
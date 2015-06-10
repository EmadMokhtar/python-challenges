def remove_characters(text, characters):
	for character in characters:
		text = text.replace(character, '')
	return text


with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		text, characters = line.strip().split(',')
		print remove_characters(text, characters.strip())
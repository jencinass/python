with open('./text.txt', 'r+') as file:
	for line in file:
		print(line)
	file.write('hello my friend this is a new text')

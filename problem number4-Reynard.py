import re

def sentence_splitter(file_name):
	with open(file_name, 'r') as f:
		file_content = f.read()

	sentences = re.sub(r'\n', '', file_content)

	sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)

	print (sentences)

sentence_splitter('text number4.txt')
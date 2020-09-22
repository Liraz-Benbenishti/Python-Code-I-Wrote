def sort(path_to_text_file):
	"""
	:param path_to_text_file: file path
	:type path_to_text_file: string
	:return: None
	rtype: None
	"""
	file_content = open(path_to_text_file, 'r').read().splitlines()

	file_content_words_list = []
	
	for line in file_content:
		file_content_words_list = file_content_words_list + line.split(" ")
		
	file_content_words_list = sorted(file_content_words_list)
	
	for word in file_content_words_list:
		for i in range(file_content_words_list.count(word) - 1):
			file_content_words_list.remove(word)
	
	print(file_content_words_list)
	
	
def rev(path_to_text_file):
	"""
	:param path_to_text_file: file path
	:type path_to_text_file: string
	:return: None
	rtype: None
	"""
	file_content = open(path_to_text_file, 'r').read().splitlines()

	for line in file_content:
		print(line[::-1])

	
def last(path_to_text_file):
	"""
	:param path_to_text_file: file path
	:type path_to_text_file: string
	:return: None
	rtype: None
	"""
	n = int(input("Enter a number: "))
	file_content = open(path_to_text_file, 'r').read().splitlines()
	
	for line_num in range(len(file_content)-n, len(file_content), 1):
		print(file_content[line_num])

	

def main():
	path_to_text_file = input("Enter a file path: ")
	action = input("Enter a task (sort, rev, last): ")
	if (action == "sort"):
		sort(path_to_text_file)
		
	if (action == "rev"):
		rev(path_to_text_file)
		
	if (action == "last"):
		last(path_to_text_file)
		
if __name__ == "__main__":
	main()
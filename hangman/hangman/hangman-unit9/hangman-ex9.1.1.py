def are_files_equal(file1, file2):
	"""
	:param file1: path for file number 1.
	:param file2: path for file number 2.
	:type file1: string
	:type file2: string
	:return: either or not the files content are identical.
	rtype: bool
	"""
	file1_content = open(file1, 'r').read()
	file2_content = open(file2, 'r').read()
	
	return file1_content == file2_content
	
def main():
	print(are_files_equal(r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\file1.txt", r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\file2.txt"))
	
if __name__ == "__main__":
	main()
	
def copy_file_content(source, destination):
	"""
	:param source: represents file pah.
	:param destination: represents file pah.
	:type source: string
	:type destination: string
	:rerturn: 
	rtype: None
	"""
	with open(source, 'r') as copy_file:
		copy_file_data = copy_file.read()
		with open(destination, 'w') as paste_file:
			paste_file.write(copy_file_data)
	
def main():
	copy_file_content(r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\copy.txt", r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\paste.txt")
	
if __name__ == "__main__":
	main()
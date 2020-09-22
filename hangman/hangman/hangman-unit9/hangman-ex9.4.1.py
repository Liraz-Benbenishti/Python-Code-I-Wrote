def choose_word(file_path, index):
	"""
	:param file_path: path to a file.
	:param index: location of word in the file.
	:type file_path: string
	:type index: int
	:return: returns a tuple with two elements: number of different words in the file (without duplicates), and a word in the location inputted.
	rtype: tuple
	"""
	with open(file_path, 'r') as words_file:
		words_list = words_file.read().splitlines()[0].split(" ")
	secret_word = words_list[(index - 1) % len(words_list)]
	words_list = sorted(words_list)
	
	for word in words_list:
		for i in range(words_list.count(word) - 1):
			words_list.remove(word)
		
	return len(words_list), secret_word
	
def main():
	print(choose_word(r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\words.txt", 3))
	print(choose_word(r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\words.txt", 15))

if __name__ == "__main__":
	main()
HANGMAN_PHOTOS = {0: """x-------x""", 
1: """x-------x
|
|
|
|
|
""",
2: """x-------x
|       |
|       0
|
|
|
""",
3: """x-------x
|       |
|       0
|       |
|
|
""", 
4: """x-------x
|       |
|       0
|      /|\\
|
|
""", 
5: """x-------x
|       |
|       0
|      /|\\
|      /
|
""", 
6: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""}

def check_win(secret_word, old_letters_guessed):
	"""
	:param secret_word: the string is the secret word the user need to guess.
	:param old_letters_guessed: the list contains the letters the player guessed.
	:type secret_word: string
	:type old_letters_guessed: list
	:return: either or not all the letters that comprised the word is contained the list of letters the player guessed, and therefore, he won the game.
	rtype: bool
	"""
	for char in secret_word:
		if (char not in old_letters_guessed):
			return False
	return True

def show_hidden_word(secret_word, old_letters_guessed):
	"""
	:param secret_word: represent the hidden word the player need to guess.
	:param old_letters_guessed: the list that contain the letters the player guessed by now.
	:type secret_word: string
	:type old_letters_guessed: list
	:return: string that comprised of the letters and underscores. Shows the letter from  the list that contained in the secret word in their location.
	rtype: string
	"""
	new_word = []
	for letter in secret_word:
		if (letter.lower() in old_letters_guessed):
			new_word.append(letter)
		else:
			new_word.append("_")
	return " ".join(new_word)

def check_valid_input(letter_guessed, old_letters_guessed):
	"""
	The function gets as parameter the string the user entered and return if the character valid or not.
	:param letter_guessed: The string the user entered.
	:param old_letters_guessed: list contains the letters the player guessed until now.
	:type letter_guessed: string
	:type old_letters_guessed: list
	:return: returns if the character is valid and the user didn't guessed it alreadyor not.
	rtype: bool
	"""
	letter_guessed = letter_guessed.lower()
	if (len(letter_guessed) > 1):
		return False
	if (not letter_guessed.isalpha()):
		return False
	if (letter_guessed in old_letters_guessed):
		return False
	return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""
	The function gets a letter the user guessed and list of old letters guessed and add to the list or print an error.
	The function returns
	:param letter_guessed: The character the player guessed.
	:param old_letters_guessed: The list contains all the letters the player guessed.
	:type letter_guessed: string
	:type old_letters_guessed: list
	:return: Either the function added the new letter to the list or not.
	rtype: bool
	"""
	if (check_valid_input(letter_guessed, old_letters_guessed)):
		old_letters_guessed.append(letter_guessed.lower())
		return True
	print("X")
	print(" -> ".join(sorted(old_letters_guessed, key=str.lower)).lower())
	return False

def print_hangman(num_of_tries):
	"""
	:param num_of_tries: represent the number of wrong tries of the player until now.
	:type num_of_tries:  int
	:return: None
	rtype: None
	"""
	print(HANGMAN_PHOTOS[num_of_tries])
	return

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

def start_page():
	"""
	:return:
	rtype: None
	"""
	HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
	
	MAX_TRIES = 6	
	print(HANGMAN_ASCII_ART,"\n", MAX_TRIES)

def hangman(secret_word):
	"""
	:param secret_word: the secret word to guess.
	:type secret_word: string
	:return:
	rtype: None
	"""
	old_letters_guessed = []
	MAX_TRIES = 6
	num_of_tries = 0
	print_hangman(num_of_tries)
	print(show_hidden_word(secret_word, old_letters_guessed))
	
	while (num_of_tries < MAX_TRIES):
		hidden_word_before = show_hidden_word(secret_word, old_letters_guessed)
		is_valid_input = False
		while (is_valid_input == False):
			letter_guessed = input("Guess a letter: ")
			is_valid_input = try_update_letter_guessed(letter_guessed, old_letters_guessed)
		hidden_word_after = show_hidden_word(secret_word, old_letters_guessed)
		if (hidden_word_before == hidden_word_after):
			print(":(")
			num_of_tries = num_of_tries + 1
			print_hangman(num_of_tries)
		print(hidden_word_after)
		if (check_win(secret_word, old_letters_guessed)):
			print("WIN")
			break
	if (num_of_tries == MAX_TRIES):
		print("LOSE")

def play_hangman():
	"""
	:return:
	rtype: None
	"""
	start_page()
	file_path = input("Enter file path: ") # list of words seperated by space.
	index = int(input("Enter index: "))
	
	print("\nLet's start!\n")

	number_of_words, secret_word = choose_word(file_path, index)
	hangman(secret_word)
	
def main():
	play_hangman()
	
if __name__ == "__main__":
	main()
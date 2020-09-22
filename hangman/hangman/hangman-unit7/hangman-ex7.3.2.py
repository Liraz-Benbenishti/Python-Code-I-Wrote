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
	
def main():
	secret_word = "friends"
	old_letters_guessed = ['m', 'p', 'j', 'i', 's' , 'k']
	print(check_win(secret_word, old_letters_guessed))
	
	secret_word = "yes"
	old_letters_guessed = ['d', 'g', 'e', 'i', 's' , 'k', 'y']
	print(check_win(secret_word, old_letters_guessed))
	
if __name__ == "__main__":
	main()
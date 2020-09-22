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
		if (letter in old_letters_guessed):
			new_word.append(letter)
		else:
			new_word.append("_")
	return " ".join(new_word)
			
	
def main():
	secret_word = "mammals"
	old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
	print(show_hidden_word(secret_word, old_letters_guessed))
	
if __name__ == "__main__":
	main()
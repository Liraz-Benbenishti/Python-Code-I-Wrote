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

def main():
	old_letters = ['a', 'b', 'c']
	print(check_valid_input('C', old_letters))
	print(check_valid_input('ep', old_letters))
	print(check_valid_input('$', old_letters))
	print(check_valid_input('s', old_letters))

if __name__ == "__main__":
	main()
def is_valid_input(letter_guessed):
	"""
	The function gets as parameter the string the user entered and return if the character valid or not.
	:param letter_guessed: The string the user entered.
	:type letter_guessed: string
	:return: returns if the character is valid or not.
	rtype: bool
	"""
	letter_guessed = letter_guessed.lower()
	if (len(letter_guessed) > 1):
		return False
	if (not letter_guessed.isalpha()):
		return False
	return True

def main():
	print(is_valid_input('a'))
	print(is_valid_input('A'))
	print(is_valid_input('$'))
	print(is_valid_input('ab'))
	print(is_valid_input('app$'))

if __name__ == "__main__":
	main()
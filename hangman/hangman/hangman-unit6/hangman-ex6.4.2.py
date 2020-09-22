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
		old_letters_guessed.append(letter_guessed)
		return True
	print("X")
	print(" -> ".join(sorted(old_letters_guessed, key=str.lower)).lower())
	return False

def main():
	old_letters = ['a', 'p', 'c', 'f']
	print(try_update_letter_guessed('A', old_letters))
	print(try_update_letter_guessed('s', old_letters))
	print(old_letters)
	print(try_update_letter_guessed('$', old_letters))
	print(try_update_letter_guessed('d', old_letters))
	print(old_letters)

if __name__ == "__main__":
	main()
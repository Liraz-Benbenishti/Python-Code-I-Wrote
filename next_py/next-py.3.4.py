import string

class UsernameContainsIllegalCharacter(Exception):
	"""
	Thrown is the username conatains illegal characters.
	"""
	def __init__(self, letter, index):
		self._letter = letter
		self._index = index
		
	def __str__(self):
		return "Username contains illegal character \"" + self._letter + "\" in index " + str(self._index)

class UsernameTooShort(Exception):
	"""
	Thrown if the username is shorter than 3 characters.
	"""
	def __init__(self, length):
		self._length = length
		
	def __str__(self):
		return "Username is too short: length " + str(self._length)

class UsernameTooLong(Exception):
	"""
	Thrown if the username is longer than 16 characters.
	"""
	def __init__(self, length):
		self._length = length
		
	def __str__(self):
		return "Username is too long: length " + str(self._length)

class PasswordMissingCharacter(Exception):
	"""
	Thrown if the password doesn't contains one of the required characters.
	"""
	def __str__(self):
		return "The password is missing a character"
	
class PasswordMissingUppercase(PasswordMissingCharacter):
	"""
	Thrown if the password doesn't contains an uppercase letter.
	"""
	def __str__(self):
		return super().__str__() + " (Uppercase)"
		
class PasswordMissingLowercase(PasswordMissingCharacter):
	"""
	Thrown if the password doesn't contains an lowercase letter.
	"""
	def __str__(self):
		return super().__str__() + " (Lowercase)"
		
class PasswordMissingDigit(PasswordMissingCharacter):
	"""
	Thrown if the password doesn't contains an digit letter.
	"""
	def __str__(self):
		return super().__str__() + " (Digit)"
		
class PasswordMissingSpecial(PasswordMissingCharacter):
	"""
	Thrown if the password doesn't contains an special letter.
	"""
	def __str__(self):
		return super().__str__() + " (Special)"

class PasswordTooShort(Exception):
	"""
	Thrown if the password is shoter than 8 characters.
	"""
	def __init__(self, length):
		self._length = length
		
	def __str__(self):
		return "Password is too short: length " + str(self._length)

class PasswordTooLong(Exception):
	"""
	Thrown if the password is longer than 40 characters.
	"""
	def __init__(self, length):
		self._length = length
		
	def __str__(self):
		return "Password is too long: length " + str(self._length)

def check_input(username, password):
	try:
		for i in range(len(username)):
			letter = username[i]
			if (not letter.isalnum() and letter != "_"):
				raise UsernameContainsIllegalCharacter(letter, i)
		
		username_length = len(username)
		if (username_length < 3):
			raise UsernameTooShort(username_length)
			
		if (username_length > 16):
			raise UsernameTooLong(username_length)
		
		password_length = len(password)
		if (password_length < 8):
			raise PasswordTooShort(password_length)
		
		if (password_length > 40):
			raise PasswordTooLong(password_length)

		is_capital_letter = False
		is_lower_letter = False 
		is_numeric_letter = False
		is_special_letter = False
		for letter in password:
			if (letter >= "A" and letter <= "Z"):
				is_capital_letter = True
			if (letter >= "a" and letter <= "z"):
				is_lower_letter = True
			if (letter.isnumeric()):
				is_numeric_letter = True
			if (letter in string.punctuation):
				is_special_letter = True
		if (not is_capital_letter):
			raise PasswordMissingUppercase
		if (not is_lower_letter):
			raise PasswordMissingLowercase
		if (not is_numeric_letter):
			raise PasswordMissingDigit
		if (not is_special_letter):
			raise PasswordMissingSpecial

	except UsernameContainsIllegalCharacter as e:
		print(e)
		#ask_creds()
	except UsernameTooShort as e:
		print(e)
		#ask_creds()
	except UsernameTooLong as e:
		print(e)
		#ask_creds()
	except PasswordMissingCharacter as e:
		print(e)
		#ask_creds()
	except PasswordTooShort as e:
		print(e)
		#ask_creds()
	except PasswordTooLong as e:
		print(e)
		#ask_creds()
	else:
		print("OK")
	finally:
		pass

def ask_creds():
	username = input("Please enter username: ")
	password = input("Please enter password: ")
	check_input(username, password)

def main():
	#ask_creds()
	check_input("1", "2")
	check_input("0123456789ABCDEFG", "2")
	check_input("A_a1.", "12345678")
	check_input("A_1", "2")
	check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
	check_input("A_1", "abcdefghijklmnop")
	check_input("A_1", "ABCDEFGHIJLKMNOP")
	check_input("A_1", "ABCDEFGhijklmnop")
	check_input("A_1", "4BCD3F6h1jk1mn0p")
	check_input("A_1", "4BCD3F6.1jk1mn0p")
	
if __name__ == "__main__":
	main()
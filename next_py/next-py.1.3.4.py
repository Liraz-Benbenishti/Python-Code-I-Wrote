password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

"""
new_password = []
for letter in password:
	if (letter.isalpha()):
		new_password.append(chr(ord(letter) + 2))
	else:
		new_password.append(letter)
print("".join(new_password))
"""
import random;p = lambda:random.choice('7♪♫♣♠♦♥◄☼☽');[print('|'.join([p(),p(),p()]),end='\r') for i in range(8 ** 5)]
print("".join([chr(ord(letter) + 2) if letter.isalpha() else letter for letter in password]))
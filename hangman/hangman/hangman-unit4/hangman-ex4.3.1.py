player_letter_guess = input("Guess a letter: ").lower()

if (len(player_letter_guess) > 1) and (not player_letter_guess.isalpha()):
	print("E3")
elif (len(player_letter_guess) > 1):
	print("E1")
elif (not player_letter_guess.isalpha()):
	print("E2")
else:
	print(player_letter_guess.lower())
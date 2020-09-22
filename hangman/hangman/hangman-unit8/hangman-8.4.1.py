HANGMAN_PHOTOS = {0: """    x-------x""", 
1: """    x-------x
    |
    |
    |
    |
    |
""",
2: """    x-------x
    |       |
    |       0
    |
    |
    |
""",
3: """    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 
4: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 
5: """    x-------x
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

def print_hangman(num_of_tries):
	"""
	:param num_of_tries: represent the number of wrong tries of the player until now.
	:type num_of_tries:  int
	:return: None
	rtype: None
	"""
	print(HANGMAN_PHOTOS[num_of_tries])
	return
	
def main():
	num_of_tries = 6
	print_hangman(num_of_tries)

if __name__ == "__main__":
	main()
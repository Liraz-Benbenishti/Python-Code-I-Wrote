string_from_user = input("Enter a word: ")
string_from_user = string_from_user.replace(" ", "")

if (string_from_user.lower() == string_from_user[::-1].lower()):
	print("OK")
else:
	print("NOT")
user_string_input = input("Please enter a string: ")
length = len(user_string_input)
print(user_string_input[:length//2].lower() + user_string_input[length//2:].upper())
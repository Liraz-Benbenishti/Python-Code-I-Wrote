def last_early(my_str):
	my_str = my_str.lower()
	last_char = my_str[-1]
	if (my_str[:-1].find(last_char) != -1):
		return True
	return False
	
print(last_early("happy birthday"))

print(last_early("best of luck"))

print(last_early("Wow"))

print(last_early("X"))
	

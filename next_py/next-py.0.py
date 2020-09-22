def combine_coins(coin, numbers):
	new_list = ""
	for number in numbers:
		new_list += str(number) + coin + ", "
	return new_list[:-2]


def main():
	print(compine_coins('$', range(5)))
	
if __name__ == "__main__":
	main()
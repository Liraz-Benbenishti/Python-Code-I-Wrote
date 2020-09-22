def combine_coins_old(coin, numbers):
	"""
	:param coin: Currnecy symbol.
	:type coin: string
	:param numbers: list ofn umbers
	:type numbers: list
	:return: New list with the numbers concatenate to the currency symbol, with comma in between.
	rtype: list
	"""
	new_list = []
	for number in numbers:
		new_list.append(coin + str(number))
	return ", ".join(new_list)

def combine_coins(coin, numbers):
	"""
	:param coin: Currnecy symbol.
	:type coin: string
	:param numbers: list ofn umbers
	:type numbers: list
	:return: New list with the numbers concatenate to the currency symbol, with comma in between.
	rtype: list
	"""
	return ", ".join([coin + str(number) for number in numbers])	
	
def main():
	print(combine_coins('$', range(5)))

if __name__ == "__main__":
	main()
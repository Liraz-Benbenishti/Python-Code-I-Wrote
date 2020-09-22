def chk_divide_four(number):
	"""
	:param: number: a number to check.
	:type number: integer
	:return: check either or not the number divided by four without remainder.
	rtype: bool
	"""
	return number % 4 == 0

def four_dividers(number):
	"""
	:param: number: 
	:type number: integer6
	:return: return a list of all the numbers from 1 to that number (include) that devided by 4 without remainer.
	rtype: list
	"""
	return list(filter(chk_divide_four, range(1, number + 1)))
	
def main():
	print(four_dividers(9))
	print(four_dividers(3))
	
if __name__ == "__main__":
	main()
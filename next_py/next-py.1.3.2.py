import functools

def is_prime(number):
	"""
	:param number: 
	:type number: integer
	:return: returns either or not the number if prime.
	rtype: bool
	"""
	return functools.reduce(lambda a, b: a and b, [False if number % x == 0 else True for x in range(2, number)])
	
def main():
	print(is_prime(42))
	print(is_prime(43))

if __name__ == "__main__":
	main()

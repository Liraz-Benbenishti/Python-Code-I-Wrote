def take_price(elem):
	return float(elem[1])
	
def sort_prices(list_of_tuples):
	"""
	:param list_of_tuples: list of tuples, in every tuple a product and it's price.
	:type list_of_tuples: list
	:return: Returns a list of tuples sorted by the price of the products from highest to lowest.
	rtype: tuple
	"""
	return sorted(list_of_tuples, key=take_price, reverse=True)
	

def main():
	products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
	print(sort_prices(products))

if __name__ == "__main__":
	main()
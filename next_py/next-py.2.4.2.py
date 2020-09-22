class BigThing:
	def __init__(self, variable):
		self._variable = variable
		
	def size(self):
		if (isinstance(self._variable, int)):
			return self._variable
		if (isinstance(self._variable, list) or isinstance(self._variable, dict) or isinstance(self._variable, str)):
			return len(self._variable)
			
class BigCat(BigThing):
	def __init__(self, variable, weight):
		super().__init__(variable)
		self._weight = weight
	
	def size(self):
		if (self._weight > 20):
			return "Very Fat"
		elif (self._weight > 15):
			return "Fat"
		else:
			return "OK"
			
def main():
	my_thing = BigThing("balloon")
	print(my_thing.size())
	cutie = BigCat("mitzy", 22)
	print(cutie.size())

if __name__ == "__main__":
	main()
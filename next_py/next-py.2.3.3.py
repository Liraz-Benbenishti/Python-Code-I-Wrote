class Octopus:
	count_animals = 0

	def __init__(self, age, name = "Octavio"):
		self._name = name
		self._age = age
		Octopus.count_animals = Octopus.count_animals + 1
		
	def birthday(self):
		self._age = self._age + 1
	
	def get_age(self):
		return self._age
	
	def set_name(self, name):
		self._name = name

	def get_name(self):
		return self._name
	
	
	
def main():
	octopus1 = Octopus(5, "Octi")
	octopus2 = Octopus(7)
	
	print(octopus1.get_name())
	print(octopus2.get_name())
	
	octopus2.set_name("New Name")
	
	print(octopus2.get_name())
	
	print(Octopus.count_animals)
	
if __name__ == "__main__":
	main()
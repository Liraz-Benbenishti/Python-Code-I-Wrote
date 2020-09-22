class Octopus:
	def __init__(self, age):
		self.name = "Ocatavio"
		self.age = age
		
	def birthday(self):
		self.age = self.age + 1
	
	def get_age(self):
		return self.age
	
def main():
	octopus1 = Octopus(5)
	octopus2 = Octopus(7)
	octopus1.birthday()
	print(octopus1.get_age())
	print(octopus2.get_age())
	
if __name__ == "__main__":
	main()
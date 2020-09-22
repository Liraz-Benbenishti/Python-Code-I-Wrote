class Animal:
	"""
	A class used to represent an animal
	"""
	zoo_name = "Hayaton"
		
	def __init__(self, name, hunger = 0):
		"""
		Creates an instance of class Animal.
		:param name: Animal's name.
		:param hunger: Animal's level of hunger.
		:type name: string
		:type hunger: int
		:return: None.
		:rtype: None
		"""
		self._name = name
		self._hunger = hunger
	
	def get_name(self):
		"""
		Get the animal's name.
		:return: Returns the animal's name.
		:rtype: string
		"""
		return self._name
	
	def is_hungry(self):
		"""
		Returns either or not the animal is hungry.
		:return: Returns either or not the animal is hungry.
		:rtype: bool
		"""
		return self._hunger > 0
	
	def feed(self):
		"""
		Decrease the animal's level of hunger by 1.
		:return: None.
		:rtype: None
		"""
		self._hunger = self._hunger - 1
	
	def talk(self):
		"""
		The animal talks.
		:return: None.
		:rtype: None
		"""
		pass
	
class Dog(Animal):
	"""
	A class used to represent an animal of type Dog.
	"""
	def talk(self):
		"""
		The dog is talking.
		:return: None.
		:rtype: None
		"""
		print("woof woof")

	def fetch_stick(self):
		"""
		Print the eating string.
		:return: None.
		:rtype: None
		"""
		print("There you go, sir!")

	def __str__(self):
		"""
		Return the type and name of the animal for Dog class.
		:return: the type and name of the animal (Dog).
		:rtype: String
		"""
		return self.__class__.__name__ +  " " + self._name
		
class Cat(Animal):
	"""
	A class used to represent an animal of type Cat.
	"""
	def talk(self):
		"""
		Prints the talk string for the Cat.
		:return: None.
		:rtype: None
		"""
		print("meow")

	def chase_laser(self):
		"""
		Print the eat string for the Cat class.
		:return: None.
		:rtype: None
		"""
		print("Meeeeow")

	def __str__(self):
		"""
		Returns the type and name of the animal for Cat class.
		:return: Type and name of the animal.
		:rtype: String
		"""
		return self.__class__.__name__ +  " " + self._name
	
class Skunk(Animal):
	"""
	A class used to represent an animal of type Skunk.
	"""
	def __init__(self, name, hunger = 0, stink_color = 6):
		"""
		Initialize the Skunk class instance.
		:param name: the name of the animal.
		:param hunger: The level of hunger of the animal.
		:param stink_color: The color of the animal.
		:type name: String
		:type hunger: Integer
		:type stink_color: Integer
		:return: None.
		:rtype: None
		"""
		super().__init__(name, hunger)
		self._stink_count = stink_color

	def talk(self):
		"""
		Print the talk string for the animal (Skunk).
		:return: None.
		:rtype: None
		"""
		print("tsssss")

	def stink(self):
		"""
		Print the stink string for the animal.
		:return: None.
		:rtype: None
		"""
		print("Dear lord!")

	def __str__(self):
		"""
		Print the type and name of the animal (Skunk).
		:return: The type and name of the animal.
		:rtype: None.
		"""
		return self.__class__.__name__ +  " " + self._name
		
class Unicorn(Animal):
	"""
	A class used to represent an animal of type Unicorn.
	"""
	def talk(self):
		"""
		Prints the talk string of the animal (Unicorn).
		:return: None.
		:rtype: None
		"""
		print("Good day, darling")

	def sing(self):
		"""
		Prints the sing string of the animal (Unicorn).
		:return: None.
		:rtype: None
		"""
		print("I'm not your toy...")
	
	def __str__(self):
		"""
		Returns the type and name of the animal (Unicorn).
		:return: Type and name of the animal.
		:rtype: String
		"""
		return self.__class__.__name__ +  " " + self._name

class Dragon(Animal):
	"""
	A class used to represent an animal of type Dragon.
	"""
	def __init__(self, name, hunger = 0, color = "Green"):
		"""
		Initialize the class instance.
		:param name: The name of the animal.
		:param hunger: The level of hunger of the animal.
		:param color: The color of the animal.
		:type name: String
		:type hunger: Integet
		:type color: String
		:return: None.
		:rtype: None
		"""
		super().__init__(name, hunger)
		self._color = color

	def talk(self):
		"""
		Prints the talk string for the animal.
		:return: None.
		:rtype: None
		"""
		print("Raaaawr")

	def breath_fire(self):
		"""
		Prints the breath fire string for the animal.
		:return: None.
		:rtype: None
		"""
		print("$@#$#@$")

	def __str__(self):
		"""
		Returns the type and name of the animal.
		:return: Type and name of the animal.
		:rtype: String
		"""
		return self.__class__.__name__ + " " + self._name

def print_zoo_list(zoo_lst):
	"""
	Prints the animals in the zoo.
	:param zoo_lst: List of zoo animals.
	:type zoo_lst: list
	:return: None.
	:rtype: None
	"""
	for animal in zoo_lst: # Loop through the animals in the zoo.
		if animal.is_hungry():
			print(animal)
			
		while animal.is_hungry(): # Feed the animal until not hungry anymore.
			animal.feed()
			
		animal.talk()
		
		# Every animal does an action depends on its type.
		if (isinstance(animal, Dog)):
			animal.fetch_stick()
		elif (isinstance(animal, Cat)):
			animal.chase_laser()
		elif (isinstance(animal, Skunk)):
			animal.stink()
		elif (isinstance(animal, Unicorn)):
			animal.sing()
		elif (isinstance(animal, Dragon)):
			animal.breath_fire()

def main():
	# Definition of the animals in the zoo.
	brownie = Dog("Brownie", 10)
	zelda = Cat("Zelda", 3)
	stinky = Skunk("Stinky", 0)
	keith = Unicorn("Keith", 7)
	lizzy = Dragon("Lizzy", 1450)
	
	zoo_lst = [brownie, zelda, stinky, keith, lizzy]
	
	doggo = Dog("Doggo", 80)
	kitty = Cat("Kitty", 80)
	stinkyjr = Skunk("Stinky Jr.", 80)
	clair = Unicorn("Clair", 80)
	mcfly = Dragon("McFly", 80)
	
	zoo_lst.extend([doggo, kitty, stinkyjr, clair, mcfly])

	print_zoo_list(zoo_lst)
	
	print(Animal.zoo_name) # Print the zoo name.

if __name__ == "__main__":
	main()
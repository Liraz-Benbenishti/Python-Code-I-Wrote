class UnderAge(Exception):
	def __init__(self, age):
		self._age = age
	
	def __str__(self):
		return "Your age is below 18. Your age is " + str(self._age) + " you can come in " + str(18 - self._age) + " years."
		
def send_invitation(name, age):
	try:
		if int(age) < 18:
			raise UnderAge(age)
		else:
			print("You should send an invite to " + name)
	except UnderAge as e:
		print(e)

def main():
	#send_invitation(17, 20)
	send_invitation("a", 17)
	send_invitation("a", 20)
	
if __name__ == "__main__":
	main()
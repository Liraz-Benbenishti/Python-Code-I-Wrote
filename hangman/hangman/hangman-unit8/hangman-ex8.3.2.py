import datetime

def print_menu():
	print("""
	1. Print Mariah's Last name.
	2. Print the month she was born.
	3. Print the number of hobbies Mariah have.
	4. Print the last hobby Mariah have.
	5. Add the hobby "Cooking" to the end of the hobby list.
	6. Convert birth day to a tuple (dd, mm, yyyy) and print it.
	7. Add new key in the name "age" that contain mariah's age.
	""")

def main():
	mariah_carrey = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}

	while (1):
		print_menu()
		option = int(input("Choose an option: "))
		if (option == 1):
			print("Mariah's last name is %s" % mariah_carrey["last_name"])
		if (option == 2):
			monthinteger = int(mariah_carrey["birth_date"][3:5])
			month = datetime.date(1900, monthinteger, 1).strftime('%B')
			print("Mariah was born in the %s" % month)
		if (option == 3):
			print("The number of hobbies mariah havs is %d" % len(mariah_carrey["hobbies"]))
		if (option == 4):
			print("The last hobby in Mariah's hobbies list is %s" % mariah_carrey["hobbies"][-1])
		if (option == 5):
			mariah_carrey["hobbies"].append("Cooking")
		if (option == 6):
			tuple1 = (day, month, year) = tuple(int(x) for x in mariah_carrey["birth_date"].split("."))
			print(tuple1)
		if (option == 7):
			mariah_carrey["age"] = datetime.datetime.now().year - int(mariah_carrey["birth_date"].split(".")[2])
			print("Mariah age is %d" % mariah_carrey["age"])

if __name__ == "__main__":
	main()
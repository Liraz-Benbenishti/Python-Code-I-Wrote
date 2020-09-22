def print_menu():
	print("""
	1. Print list of groceries.
	2. Print number of groceries in the list.
	3. Check if item is in the list.
	4. How many times an item appear in the list.
	5. Remove product to the list.
	6. Add product to the list.
	7. Print all ilegal groceries (length smaller than 3 or contains non-letters characters.)
	8. Remove all Duplicates from list.
	9. Exit
	""")





def main():
	string_from_user = input("Enter list of groceries to buy seperated by comma: ")
	# "Milk,Cottage,Tomatoes"
	list_of_groceries = string_from_user.split(',')
	while (1):
		print_menu()
		option = int(input("Choose an option: "))
		if (option == 1):
			print("List of groceries: " + ", ".join(list_of_groceries))
		if (option == 2):
			print("The number of groceries are " + str(len(list_of_groceries)))
		if (option == 3):
			look_for_groceries = input("Enter name of grocery to look for: ")
			print(look_for_groceries in list_of_groceries)
		if (option == 4):
			grocery_count = input("Enter name of grocery to count: ")
			print(list_of_groceries.count(grocery_count))
		if (option == 5):
			grocery_to_delete = input("Enter name of grocery to delete: ")
			if (grocery_to_delete in list_of_groceries):
				list_of_groceries.remove(grocery_to_delete)
		if (option == 6):
			add_grocery_to_list = input("Enter name of grocery to add: ")
			list_of_groceries.append(add_grocery_to_list)
		if (option == 7):
			for grocery in list_of_groceries:
				if (len(grocery) < 3 or not grocery.isalpha()):
					print(grocery)
		if (option == 8):
			for grocery in list_of_groceries:
				for i in range(list_of_groceries.count(grocery) - 1):
					list_of_groceries.remove(grocery)
		if (option == 9):
			break
if __name__ == "__main__":
	main()
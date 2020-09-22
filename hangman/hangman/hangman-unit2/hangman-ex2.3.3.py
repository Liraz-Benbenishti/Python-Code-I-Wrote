bricks_pigs = int(input("Enter the amount of bricks the pigs got: "))
pig1 = bricks_pigs % 10
pig3 = int(bricks_pigs / 100)
pig2 = int((bricks_pigs - pig3 * 100 - pig1) / 10)
total = pig1 + pig2 + pig3
print("The total amount of bricks the pigs have:", total)
print("The average amount of bricks: ", int(total / 3))
print("The remainer of bricks: ", total % 3)
print(total % 3 == 0)
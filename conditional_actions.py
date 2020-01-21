# Get a number from a user
number = int(input("Enter a number:"))

# If number is odd, print Weird
if (number % 2 != 0):
    print("Weird")

# If number is even and in the inclusive range of 2 to 5, print Not Weird
elif ((number % 2 == 0) and (number in  range(2, 5))):
    print("Not Weird")

# If number is even and in the inclusive range of 6 to 20, print weird
elif ((number % 2 == 0) and (number in range (6, 20))):
    print("Weird")

# If number is even and greater than 20, print Not Weird
elif ((number % 2 == 0) and (number > 20)):
    print("Not Weird")

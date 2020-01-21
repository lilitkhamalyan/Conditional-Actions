number = int(input("Enter a number:"))
if (number % 2 != 0):
    print("Weird")

elif ((number % 2 == 0) and (number in  range(2, 5))):
    print("Not Weird")

elif ((number % 2 == 0) and (number in range (6, 20))):
    print("Weird")

elif ((number % 2 == 0) and (number > 20)):
    print("Not Weird")

import sys
# prompts the user to enter year of birth

birthyear = input("Enter year of birth")
# calculates the age of the user
age = int(2023) - int(birthyear)
print(age)

# enables the user to enter there height in meters
height = input("Enter height in meters")
print(height)

# display the datatype of the input
print(type(birthyear))
print(type(age))
print(type(height))

# display the size of the input
print(sys.getsizeof(birthyear))
print(sys.getsizeof(age))
print(sys.getsizeof(height))
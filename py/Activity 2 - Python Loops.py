#Write a Python program to create the multiplication table (from 1 to 10) of a number.
print("Easy program to show the multiplication table from 1 to 10")
number_1 = int(input("Please input the number:"))
#create a variable to acumulate the cicles
x = 0
#define the cicle for
for x in range (1,11):
    # Calculate the product of the number and the loop variable
    result = number_1 * x
    # Print the multiplication table
    print(f"{number_1} x {x} = {result}")
# Write a Python function to calculate the factorial of a number (a non-negative integer n ).
# The function accepts the number as an argument.

number = int(input("Input a non-negative number to calculate factorial: "))
x = 1

def factorial_function(number):
    if number < 0:
        print("Invalid input. Number is negative.")
    elif number == 0:
        print("Factorial is: 1")  # Factorial of 0 is 1
    else:
        x = 1  # Reset x to 1 for each function call
        for i in range_1:
            x *= i  # Update x with the product of x and i
        return x

range_1 = range(1, number + 1) # Create a variable to store the range

# Print every number in the same line with an asterisk (*) between them and ending in * to make it look like a factorial operation using , to separate it
print(f"The factorial result of {number}! is ", *range_1, sep="*", end="!")

factorial_result = factorial_function(number)
print(f" = {factorial_result}")

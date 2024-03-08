#Write a Python function that takes a number as a parameter and check the number is prime or not.

# Take user input for the number to check for primality
x = int(input("Enter a number to check if it is prime:"))

# Define a function to check if a number is prime
def function_is_prime(x):
    # Check if the number is negative
    if x < 0:
        print("Negative numbers cannot be prime")
    # Check if the number is 1
    elif x == 1:
        print("1 is not prime")
    else:
        # Assume the number is prime initially
        is_prime = True
        # Check for factors starting from 2 up to x
        for i in range(2, x):
            # If i is a factor of x, set is_prime to False and break the loop
            if x % i == 0:
                is_prime = False
                print(f"{x} is divisible by {i} with no remainder; therefore, it is not prime.") # A quick explanation with an argument
                break
        # Print the result based on the is_prime variable
        if is_prime:
            print(f"{x} is prime")

# Call the function with the user-provided number
function_is_prime(x)

#




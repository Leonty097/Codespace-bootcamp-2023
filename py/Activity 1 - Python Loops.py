#Write a Python program to get the Fibonacci series between 0 to 50.
print("Fibonacci series from 0 to 50")
# We need two consecutives numbers to start the secuence a & b in this case
a = 0
b = 1
# Create a ehile loop for the range 0 to 50
while a < 50:
    print(a)
# We use a third variable called c to acumulate the sum and create a serie to replicate fibonacci adding the other two variables (a & b) before it
    c = a
    a = b
    b = c + b


print("Easy program to compare three numbers:")
number_1 = int(input("Input first number:"))
number_2 = int(input("Input second number:"))
number_3 = int(input("Input third number:"))

if number_1 == number_2 == number_3:
    print("All numbers are equal")
elif (number_1 == number_2 != number_3) or (number_1 != number_2 == number_3):
    print("Two of three numbers are equals")
else:
    print("All numbers are different")

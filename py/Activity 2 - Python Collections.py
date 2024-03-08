#Write a Python program to calculate the average value of a list elements.

# Take input from the user, assuming numeric elements are separated by commas
user_raw_input = input("Add numeric elements separated by commas to know the average: ")

# Split the input string based on commas and create a list
my_list = user_raw_input.split(",")

# Convert the elements to integers
my_list = [int(x) for x in my_list]

print("List of numeric elements:", my_list)

average =  round(sum(my_list) / len(my_list),1)
print(f"Average value of the list element is: {average}")
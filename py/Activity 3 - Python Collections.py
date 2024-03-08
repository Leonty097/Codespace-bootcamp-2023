# Write a Python program to find the maximum and minimum value of a list.


# Take input from the user, assuming numeric elements are separated by commas
user_raw_input = input("Add numeric elements separated by commas: ")

# Split the input string based on commas and create a list
my_list = user_raw_input.split(",")

# Convert the elements to integers
my_list = [int(x) for x in my_list]

print("List of numeric elements:", my_list)
# Define Max and Min values, I initially though that starting them in 0 will work but had issues with negative values so I searched and found that you can use infite so:
max_value = float("-inf")
min_value = float("inf")
# Count the length of the list
my_list_len = len(my_list)
#use the lentgh to define the range
for x in range (0,my_list_len):
    #Pop element by element and sum them
    popped_element = my_list.pop()
    #print(popped_element)
    #print(my_list)
    if popped_element > max_value:
        max_value = popped_element
        #popped_element = max_value

    if popped_element < min_value:
        min_value = popped_element

  #show result
print(f"The Maximun value is = {max_value}")
print(f"The Minimum value is = {min_value}")



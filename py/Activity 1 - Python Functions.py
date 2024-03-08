#Write 2 Python functions to:
# show the list content.
# find the max value in the list.

# Get numeric input from the user, assuming elements are separated by commas
user_raw_input = input("Add numeric elements separated by commas: ")

# Split the input string based on commas and create a list
my_list = user_raw_input.split(",")

# Convert the elements to integers
my_list = [int(x) for x in my_list]
compare_value = 0  # Initialize a comparison value

def function_show():
    # Display the content of the list
    print(f"The content of the list is: {my_list}")
# Call the function to display the list content
function_show()
def function_max_value():
    max_value = my_list[0]  # Start with the first element as the maximum
    for value in my_list:  # Loop through each element in the list
        if value > max_value:  # Compare the current value with the current maximum
            max_value = value  # Update the maximum if the current value is greater
    return max_value  # Return the maximum value found

# Print the maximum value found by the function
print(f"The max value is: {function_max_value()}")



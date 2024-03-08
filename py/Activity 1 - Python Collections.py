# Write a Python program to sum values of a list.
#Unnecessary long way, completely avoiding the quite appropriate sum(my_list)


# Take input from the user, assuming numeric elements are separated by commas
user_raw_input = input("Add numeric elements separated by commas to know the sum of them: ")

# Split the input string based on commas and create a list
my_list = user_raw_input.split(",")

# Convert the elements to integers
my_list = [int(x) for x in my_list]

print("List of numeric elements:", my_list)
# Create an acumulative variable starting on 0
sum_acumulative = 0
# Count the length of the list
my_list_len = len(my_list)
#use the lentgh to define the range
for x in range (0,my_list_len):
    #Pop element by element and sum them
    popped_element = my_list.pop()
    sum_acumulative += int(popped_element)
    #print(popped_element)
    #print(my_list)
    #print(sum_acumulative)
    #show result
final_result = sum_acumulative
print(f"The sum of those elements is = {sum_acumulative}")
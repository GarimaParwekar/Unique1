def unique(input_list=[]):
    to_return = []
    for el in input_list:
        if el not in to_return:
            to_return.append(el)
    return to_return

# Prompt the user to enter a list of elements, separated by commas
user_input = input("Please enter a list of numbers, separated by commas (e.g., 1,2,3,4,5,5,5,6): ")

# Convert the user input into a list of integers
input_list = [int(item.strip()) for item in user_input.split(',')]

# Invoke the unique function
unique_elements = unique(input_list)

# Print the unique elements
print("Unique elements are:", unique_elements)



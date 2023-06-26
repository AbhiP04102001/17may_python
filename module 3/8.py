# Write a Python function that takes a list and returns a new list with unique
elements of the first list. 
input_list = [1, 2, 2, 3, 3, 4, 5, 5]

unique_list = []

for element in input_list:
    if element not in unique_list:
        unique_list.append(element)

print(unique_list)

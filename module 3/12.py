# Write a Python program to get unique values from a list
my_list = [1, 2, 3, 2, 4, 3, 5, 6, 5, 4]

unique_list = []

for item in my_list:
    if item not in unique_list:  
        unique_list.append(item) 


print("Unique values:", unique_list)

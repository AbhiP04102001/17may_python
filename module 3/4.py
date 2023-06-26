# Write a Python program to remove duplicates from a list. 
my_list = [1,4,1,3,2,5,2,1,6,2,9,8]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

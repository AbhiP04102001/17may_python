# Write a Python program to find the second smallest number in a list. 
my_list = [5, 2, 9, 55, 7, 3, 6, 8, 4]

smallest = float('inf')  
second_smallest = float('inf')  

for num in my_list:
    if num < smallest: 
        second_smallest = smallest  
        smallest = num  
    elif num < second_smallest and num ! = smallest: 
        second_smallest = num  

print("Second smallest number:", second_smallest)

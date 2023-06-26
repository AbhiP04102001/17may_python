# Write a Python function that takes two lists and returns true if they have
at least one common member. 
list1 = [1, 2, 3, 4, 11]
list2 = [5, 6, 7, 8, 9]

set1 = set(list1)
set2 = set(list2)

if set1.intersection(set2):
    print(True)
else:
    print(False)

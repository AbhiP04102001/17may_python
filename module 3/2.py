# Write a Python function to get the largest number, smallest num and sum
of all from a list
numbers = [22,55,42,84,66,37]

largest = float('-inf')
smallest = float('inf')
total = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total += num

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", total)

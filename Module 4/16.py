# Write a Python program to create a tuple with numbers
numbers = []

n = int(input("Enter the number of elements in the tuple: "))

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    numbers.append(num)

tuple_numbers = tuple(numbers)

print("Tuple:", tuple_numbers)

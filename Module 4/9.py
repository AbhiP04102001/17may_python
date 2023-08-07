# Write a Python program to convert a list of characters into a string
char_list = ['H', 'e', 'l', 'l', 'o']

string = ""
for char in char_list:
    string += char

print(string)  


string = "".join(char_list)
print(string)  

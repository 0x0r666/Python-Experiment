

#Aim: Write a program to implement various string operations.


s = input("Enter a string: ")

# Reverse
print("Reverse:", s[::-1])

# Count / Length
print("Length:", len(s))

# Palindrome check
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Uppercase
print("Uppercase:", s.upper())

# Lowercase
print("Lowercase:", s.lower())

# Capitalize
print("Capitalize:", s.capitalize())

# Swapcase
print("Swapcase:", s.swapcase())

# Find position of 'a'
print("Position of 'a':", s.find('a'))

# Replace 'a' with '@'
print("Replace 'a' with '@':", s.replace('a', '@'))

# Split words
print("Split words:", s.split())

# Check membership
print("'z' not in string:", 'z' not in s)

# First and Last character
print("First character:", s[0])
print("Last character:", s[-1])

# Check substring existence
sub = "e"
if sub in s:
    print("'e' exists in the string")
else:
    print("'e' does not exist in the string")
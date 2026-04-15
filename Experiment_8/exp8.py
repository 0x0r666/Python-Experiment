# Aim: Implement ‘re’ module in python

import re
text = input("Enter a string: ")
# searching
result = re.search("Python", text)
print("Search 'Python':", "Found" if result else "Not Found")
# finding all digits
digits = re.findall(r'\d', text)
print("Digits in string:", digits)

# replacing
new_text = re.sub("Python", "Java", text)
print("After Replace:", new_text)

# splitting
words = re.split(r'\s', text)
print("Split words:", words)

# match check from beginning
result = re.match("Python", text)
print("Match 'Python' at start:", "Matched" if result else "Not Matched")



#Aim: Write a program to demonstrate tuple & related functions in python.

phonebook={}
n=int(input("Enter how many numbers: "))
for i in range(n):
    name,number = input("Enter name and number: ").split()
    phonebook[name]=number
print("Original List")
print(phonebook)
#get()
search=input("Enter name to search: ")
print("Their Contact no: ",phonebook.get(search,"Contact not found"))
#keys()
print("All names")
print(phonebook.keys())
#values()
print("All numbers")
print(phonebook.values())
#items
print("Contacts")
print(phonebook.items())
#copy()
phonebook2=phonebook.copy()
print("Copied")
print(phonebook2)
#update()
update_name=input("Enter name of number to update")
if update_name in phonebook:
    new_number=int(input("Enter number: "))
    phonebook.update({update_name:new_number})
    print("After: ",phonebook)
else:
    print("Not there")
#delete()
del_name=input("Enter name to delete: ")
if del_name in phonebook:
    del phonebook[del_name]
else:
    print("Not there: ")
#pop()
pop_name=input("Enter name to pop: ")
removed=phonebook.pop(pop_name,None)
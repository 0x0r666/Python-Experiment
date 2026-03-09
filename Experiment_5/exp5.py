

#Aim: Write a program to demonstrate tuple & related functions in python.


t1,t2,t3 = (1,2,3),(250,36,200),("Apple","Banana","Watermelon","Dragon Fruit")
print("Original tuple",t1,t2,t3)

#access elements
print("First element of t1: ",t1[0])
print("Second element of t1: ",t1[2])
print("Third element of t1: ",t1[2])
#length of tuple
print("length of tuple 1: ",len(t1))
print("length of tuple 2: ",len(t2))
print("length of tuple 3: ",len(t3))
#Nested
nested_tuple = (t1,t3)
print("Nested: ",nested_tuple)
#concat
t4 = t2+t3
print("Concatenation: ",t4)
#Membership
print("Membership: ")
print("Is 2 in t1?",2 in t1)
print("Is Mango in t3","Mango" in t3)
#if/else
word = input("Enter fruit name to check")
if word in t3:
    print(word,"is present")
else:
    print(word,"not present")
#Built-In Function
int = (98,28,23,10,4,10,48,84,19)
print("Max: ",max(int))
print("Min: ",min(int))
print("Sum: ",sum(int))
#count
print("Occurance of number 10: ",int.count(10))
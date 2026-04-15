# Aim: Demonstrate use of object- oriented programming concepts

# -------- CLASS & METHOD --------
class Person:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("Name:", self.name)

# -------- SINGLE INHERITANCE --------
class Student(Person):
    def display(self):
        print(self.name, "is a Student")

# -------- MULTIPLE INHERITANCE --------
class Sports:
    def sport(self):
        print("Plays Football")

class Result(Student, Sports):
    def result(self):
        print(self.name, "passed exam")

# -------- MULTILEVEL INHERITANCE --------
class A:
    def one(self):
        print("Parent Class")

class B(A):
    def two(self):
        print("Child Class")

class C(B):
    def three(self):
        print("Grandchild Class")

# -------- HIERARCHICAL INHERITANCE --------
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

# -------- MAIN --------
print("----- Class & Method -----")
p = Person("Kaustubh")
p.show()

print("\n----- Single Inheritance -----")
s = Student("Rahul")
s.show()
s.display()

print("\n----- Multiple Inheritance -----")
r = Result("Amit")
r.display()
r.sport()
r.result()

print("\n----- Multilevel Inheritance -----")
c = C()
c.one()
c.two()
c.three()

print("\n----- Hierarchical Inheritance -----")
d = Dog()
ct = Cat()
d.sound()
d.bark()
ct.sound()
ct.meow()
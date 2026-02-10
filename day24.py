# Polymorphism
# poly means many ,morphism means actions
# here poly morphism means one method / function can perform different actions based on different inputs

#same function performing different action for different inputs
def add(x,y):
    return x + y
print(add(4,6))
print(add("Puppala","Komal"))   #string concatination

# types of polymorphism
#   1. run time polymorphism (method overriding )
#   2. compile time polymorphism (method overloading)

# Method overriding
# Person
class Person():
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
    def show(self):
        return f"My name is {self.name}, my age is {self.age} years"
# Student    
class Student(Person): 
    def __init__(self,name:str,age:int,std:int):
        # super().__init__(name,age,std)
        Person.__init__(self,name,age)
        self.std=std
    def show(self):
        return f"My name is {self.name}, my age is {self.age} years and I am in {self.std} class"
p=Person("Dhanush",10)
s=Student("Komal",12,6)
print(p.show())
print(s.show())

# inheriting the parent class methods in child class using super 
class Person():
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
    def show(self):
        return f"My name is {self.name}, my age is {self.age} years"
# Student    
class Student(Person): 
    def __init__(self,name:str,age:int,std:int):
        # super().__init__(name,age,std)
        Person.__init__(self,name,age)
        self.std=std
    def show(self):
        print(super().show())
        return f"My name is {self.name}, my age is {self.age} years and I am in {self.std} class"
p=Person("Dhanush",10)
s=Student("Komal",12,6)
# print(p.show())
print(s.show())

# Method Overloading
#    Single class have multiple methods with samename with different parameter list
class maths():
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,b,c,d):
        return a+b+c+d
m=maths()
print(m.add(1,2,3,4))
print(m.add(1,2,3))
print(m.add(1,2))
# Hence last created method is stored 

# overcoming method overloading using default args (or) varible len pos args (or) var len keyword args
class maths():
    def add(self,a,b,c=0,d=0,*args):
        print(type(args))
        return a+b+c+d
m=maths()
print(m.add(1,2,3,4,5,6,7))
print(m.add(1,2,3))
print(m.add(1,2))



# ----------------------------------------------------------Library Mngmt-----------------------------------------------------------------------------------------
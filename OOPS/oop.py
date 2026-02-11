class Dog :
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.species)
print(dog1.age)

class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla" 
        self.year = 2020

car = Car()
print(car.make)
print(car.model)
print(car.year)

class MyClass:
    def display(self):
        print("Hello World")
class Student :
    def __init__(self,name,roll,branch):
        self._name = name 
        self._roll = roll
        self._branch = branch

    def _displayRollAndBranch(self):
        print("Roll :", self._roll)
        print("Branch :", self._branch)

class Geek(Student):
    def displayDetails(self):
        print("Name :", self._name)
        self._displayRollAndBranch()

obj = Geek("R2J", 1706256, "IT")
obj.displayDetails()

class Geeks :
    def __init__(self, name, roll, branch) :
        self.__name = name
        self.__roll = roll
        self.__branch = branch 

    def __displayDetails(self):
        print("Name :", self.__name)
        print("Roll :", self.__roll)
        print("Branch :", self.__branch)

    def accessPrivateFunction(self):
        self.__displayDetails()

obj = Geeks("R2J", 1706256, "CSE")

obj.accessPrivateFunction()
print(obj._Geeks__name)

class Super:
    publicData = "Public Data Member"
    _protectedData = "Protected Data Member"
    __privateData = "Private Data Mmember"

    def accessPrivateMembers(self):
        print("Accessing inside class : ", self.__privateData)

class Sub(Super) :
    def accessProtectedMembers(self):
        print("Accessing isnide subclass :", self._protectedData)

obj = Sub()

print(obj.publicData)

print(obj._protectedData)

obj.accessPrivateMembers()

print(obj._Super__privateData)

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def show_role(self):
        print(self.name, "is an employee")

emp = Employee("Sarah")
print("Name:", emp.name)
emp.show_role()
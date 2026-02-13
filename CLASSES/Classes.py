#defining a class
class Dog:
    sound = "bark" #class attribute

dog1 = Dog() # Creating object from class
print(dog1.sound) # Accessing the class

class Dog:
    def __init__(self, name, age):     #initializing object's attributes
        self.name = name    #dog's name
        self.age = age      #dog's age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
#two dog objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)
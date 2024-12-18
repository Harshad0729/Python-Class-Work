'''
Inheritance is a fundamental concept in onject-oriented programming(OOP's)
that allows a class (child class) to inherit attributes and methods from
another class (parent class).

This promotes code reuse and helps structure programs in a hierarchical manner.
Syntax:
class ParentClass:
    # Parent class implementation
    
class ChildClass(ParentClass):
    # Child class implementation
'''

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return f"{self.name} makes a sound"

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class constructor
        super().__init__(name)
        self.breed = breed
        
    def speak(self):
        # Override the speak method to make it specific to Dog
        return f"{self.name} barks!"
    
    def display_info(self):
        return f"{self.name} is a {self.breed}."

# Another Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # Call the parent class constructor
        super().__init__(name)
        self.color = color
        
    def speak(self):
        # Override the speak method to make it specific to Cat
        return f"{self.name} meows!"
    
    def display_info(self):
        return f"{self.name} is a {self.color} cat."

# Creating objects of both Dog and Cat classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "White")

# Accessing the methods from both parent and child classes
print(dog.speak())  # Dog barks
print(dog.display_info())  # Displays dog's info

print(cat.speak())  # Cat meows
print(cat.display_info())  # Displays cat's info

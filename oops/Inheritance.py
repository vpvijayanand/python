#Inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Child classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Instantiate the Dog and Cat classes
my_dog = Dog("Rex")
my_cat = Cat("Whiskers")

# Call the speak method
print(my_dog.speak())
print(my_cat.speak())

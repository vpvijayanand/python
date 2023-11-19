#Basic Class, Object, Attributes, and Methods
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Instantiate the Dog class
my_dog = Dog("Rex", 4)

# Access the instance attributes
print(f"{my_dog.name} is {my_dog.age} years old.")

# Is Rex a Canis familiaris?
print(f"Is Rex a {my_dog.species}? Yes!")

# Call our instance methods
print(my_dog.description())
print(my_dog.speak("Woof Woof"))

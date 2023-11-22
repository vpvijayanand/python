# Base class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic sound")

# First derived class
class Dog(Animal):
    def __init__(self, name, species="Dog"):
        super().__init__(species)
        self.name = name

    def make_sound(self):
        print("Bark!")

# Second derived class
class Cat(Animal):
    def __init__(self, name, species="Cat"):
        super().__init__(species)
        self.name = name

    def make_sound(self):
        print("Meow")

# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using methods from the derived classes
dog.make_sound()  # Output: Bark!
cat.make_sound()  # Output: Meow

# Accessing the species attribute from the base class
print(f"{dog.name} is a {dog.species}.")  # Output: Buddy is a Dog.
print(f"{cat.name} is a {cat.species}.")  # Output: Whiskers is a Cat.

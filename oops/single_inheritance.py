# Parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic sound")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(species)  # Call the constructor of the parent class
        self.name = name

    def make_sound(self):
        print("Bark!")

# Creating an instance of Dog
my_dog = Dog("Buddy", "Canine")

# Accessing methods from the parent class
print(f"My dog is a {my_dog.species}.")
my_dog.make_sound()  # This will use the make_sound method from the Dog class

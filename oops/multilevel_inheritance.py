# Base class
class Grandparent:
    def __init__(self, grandparent_name):
        self.grandparent_name = grandparent_name

    def gardening(self):
        print("Enjoys gardening")

# Intermediate class
class Parent(Grandparent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)
        self.parent_name = parent_name

    def reading(self):
        print("Enjoys reading")

# Derived class
class Child(Parent):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)
        self.child_name = child_name

    def playing(self):
        print("Enjoys playing")

# Creating an instance of Child
child = Child("Grandpa Smith", "Mr. Smith", "Junior Smith")

# Accessing properties and methods from the base and intermediate classes
print(f"My grandparent is {child.grandparent_name}, parent is {child.parent_name}, and my name is {child.child_name}.")
child.gardening()
child.reading()
child.playing()

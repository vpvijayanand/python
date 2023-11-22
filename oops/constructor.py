"""
In this example:
The Person class has an __init__ method, which is its constructor.
The constructor takes three arguments: self, name, and age. The self argument is a reference to the current instance of the class and is used to access variables that belong to the class.
When we create a new Person object (person1 = Person("Alice", 30)), the __init__ method is automatically called with the arguments "Alice" and 30.
Inside the constructor, self.name and self.age are set to the values passed during object creation. These are instance attributes.
The greet method can then use these attributes (self.name and self.age).
The constructor (__init__) plays a crucial role in setting up new objects with their initial state by assigning values to their attributes.
"""
class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute 'name' is initialized with the passed argument 'name'
        self.age = age    # Attribute 'age' is initialized with the passed argument 'age'

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Using the greet method of the person1 object
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.

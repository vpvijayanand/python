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

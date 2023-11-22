# First parent class
class Father:
    def __init__(self):
        self.father_name = "Mr. Smith"
    
    def gardening(self):
        print("Enjoy gardening")

# Second parent class
class Mother:
    def __init__(self):
        self.mother_name = "Mrs. Smith"
    
    def cooking(self):
        print("Enjoy cooking")

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Junior Smith"

    def sports(self):
        print("Enjoy playing football")

# Creating an instance of Child
child = Child()

# Accessing methods from parent classes
print(f"Child's parents are {child.father_name} and {child.mother_name}.")
child.gardening()
child.cooking()
child.sports()

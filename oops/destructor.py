"""
 A destructor is a method that is called when an object is about to be destroyed. 
 The destructor method is defined using the __del__ method. It's important to note that in Python, 
 due to its garbage collection mechanism, the exact time when the destructor is called is not deterministic. 
 The destructor is called when the object's reference count drops to zero, which means it's no longer needed.
 """
class SampleClass:
    def __init__(self):
        print("Constructor: Object is created")

    def __del__(self):
        print("Destructor: Object is destroyed")

# Creating an instance of SampleClass
obj = SampleClass()

# Deleting the object
del obj

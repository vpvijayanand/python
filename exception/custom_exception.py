#Custom Exception Handling
class MyCustomError(Exception):
    """A custom exception class."""
    pass

try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print(f"Caught an error: {e}")

import array

# Define a basic class
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

# Function to demonstrate file operations
def file_operations():
    try:
        # Writing to a file
        with open('example.txt', 'w') as file:
            file.write("This is a test file.\n")
            file.write("Python is fun!")

        # Reading from the file
        with open('example.txt', 'r') as file:
            content = file.read()
            print("\nFile Content:\n", content)

    except IOError as e:
        print(f"File error: {e}")

# Main function
def main():
    # Tuples and Dictionaries
    my_tuple = (1, 2, 3)
    my_dict = {'name': 'Alice', 'age': 30}

    # Array
    my_array = array.array('i', [1, 2, 3, 4])

    # Using the Greeter class
    greeter = Greeter("John")
    print(greeter.greet())

    # Working with data structures
    print("\nTuple:", my_tuple)
    print("Dictionary:", my_dict)
    print("Array:", my_array.tolist())  # Converting array to list for easy viewing

    # File operations
    file_operations()

if __name__ == "__main__":
    main()

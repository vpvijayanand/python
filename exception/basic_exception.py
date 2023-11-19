#Basic Exception Handling
try:
    # Try to convert a string to an integer
    number = int(input("Enter a number: "))
except ValueError:
    # Handle the exception if the input is not a number
    print("That's not a valid number!")
else:
    # This block runs if there is no exception
    print(f"You entered the number {number}")
finally:
    # This block always executes, regardless of an exception
    print("Execution complete.")

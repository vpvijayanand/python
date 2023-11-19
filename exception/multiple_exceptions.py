#Handling Multiple Exceptions
try:
    result = 10 / int(input("Enter a divisor: "))
except ValueError:
    print("You must enter a number!")
except ZeroDivisionError:
    print("Division by zero is not allowed!")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")

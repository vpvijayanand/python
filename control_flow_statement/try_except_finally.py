# try, except, finally
print("\n\nTry, Except, Finally:")
try:
    risky_operation = 10 / 0
except ZeroDivisionError:
    print("Caught a division by zero!")
finally:
    print("This block always executes.")

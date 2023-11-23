# assert statement (for debugging)
print("\nAssert Statement:")
x = 5
assert x == 5, "x should be 5"

print("\nAll control flow statements demonstrated!")

#Another example
def divide(x, y):
    assert y != 0, "Argument 'y' must not be zero."
    return x / y

# This will work
result = divide(10, 2)
print(result)

# This will raise an AssertionError
result = divide(10, 0)


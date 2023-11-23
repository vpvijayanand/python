# for loop
"""
print("\nFor Loop:")
for i in range(5):
    print(i, end=",")

#Increasing Values
for i in range(1, 11):
    print(i)


#Decreasing Values
for i in range(10, 0, -1):
    print(i)

#Odd Numbers
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
#Even Numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
#Skipping Values
for i in range(1, 21, 3):
    print(i)

# Iterating Over a String
for char in "Hello":
    print(char)

#Iterating Over a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Iterating Over a Dictionary
my_dict = {"name": "Alice", "age": 25}
for key, value in my_dict.items():
    print(f"{key}: {value}")

#Nested Loops
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i = {i}, j = {j}")

#Loop with enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
"""
#Looping Over Two Lists Using zip()
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(f"Number: {num}, Letter: '{letter}'")



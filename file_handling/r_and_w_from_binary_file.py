# Reading from a binary file
with open('example.jpg', 'rb') as file:
    content = file.read()

# Writing to a binary file
with open('copy_example.jpg', 'wb') as file:
    file.write(content)

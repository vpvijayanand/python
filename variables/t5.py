#The global Keyword
#You can use the global keyword to declare a variable as global inside a function.
def myfunc():
    global x
    x = 300

myfunc()
print(x)  # This will print 300

# if, elif, else
number = 15
if number > 20:
    print("Number is greater than 20.")
elif number < 20:
    print("Number is less than 20.")
else:
    print("Number is 20.")


#Using Dictionary to Mimic Switch-Case
def switch_case(argument):
    switcher = {
        1: "Case 1: January",
        2: "Case 2: February",
        3: "Case 3: March",
        # Add more cases as needed
    }
    # Get the function from switcher dictionary
    return switcher.get(argument, "Invalid case")

# Test the function
print(switch_case(1))
print(switch_case(3))
print(switch_case(5))  # This will return 'Invalid case'


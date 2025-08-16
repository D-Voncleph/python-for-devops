# Prompt the user for input and store it in a variable
user_input = input("Please enter a number or a string: ")

# Use the .isdigit() string method to check if the input contains only digits
if user_input.isdigit():
    print("You entered a number.")
else:
    print("You entered a string.")
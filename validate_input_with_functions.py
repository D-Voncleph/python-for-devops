# Part 1: Define a function to get and return user input
def get_user_input():
    """
    Prompts the user for input and returns the value.
    """
    try:
        user_input = input("Please enter something: ")
        return user_input
    except Exception as e:
        # Handle potential input errors
        print(f"An error occurred: {e}")
        return None

# Part 2: Define a function to process the input
def process_input(input_value):
    """
    Checks if the input value is a number or a string.
    """
    if input_value is None:
        return

    if input_value.isdigit():
        print(f"The input '{input_value}' is a number.")
    else:
        print(f"The input '{input_value}' is a string.")

# The main part of the script that calls the functions
if __name__ == "__main__":
    # First, call the function to get the user's input
    user_data = get_user_input()

    # Then, pass that input to the processing function
    process_input(user_data)
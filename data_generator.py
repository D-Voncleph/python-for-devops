import random

# A list of fake names to choose from for our customers
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Sarah", "Michael", "Olivia"]
last_names = ["Doe", "Smith", "Jones", "Williams", "Brown", "Davis", "Wilson", "Taylor"]

# A list to store all of our customer dictionaries
customers = []

# Use a for loop to generate 50 customer dictionaries
for i in range(50):
    # Generate a unique ID using the loop counter
    customer_id = i + 1

    # Pick a random first name and last name
    first = random.choice(first_names)
    last = random.choice(last_names)

    # Combine the first and last name to create the customer's name
    name = f"{first} {last}"

    # Generate a simple email address
    email = f"{first.lower()}.{last.lower()}@example.com"

    # Create a dictionary for the current customer
    customer = {
        "id": customer_id,
        "name": name,
        "email": email
    }

    # Add the new customer dictionary to our list of customers
    customers.append(customer)

# Print the final list of dictionaries to the console
for customer in customers:
    print(customer)
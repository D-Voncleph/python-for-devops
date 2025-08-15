import random

# A list of fake names to choose from
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Sarah"]
last_names = ["Doe", "Smith", "Jones", "Williams", "Brown", "Davis"]

# A list to store the generated usernames
generated_usernames = []

# Use a for loop to generate 10 usernames
for i in range(10):
    # Pick a random first name and last name
    first = random.choice(first_names)
    last = random.choice(last_names)
    # Combine them with a random number and add to our list
    username = f"{first.lower()}_{last.lower()}_{random.randint(100, 999)}"
    generated_usernames.append(username)

# Print the final list to the console
print(generated_usernames)
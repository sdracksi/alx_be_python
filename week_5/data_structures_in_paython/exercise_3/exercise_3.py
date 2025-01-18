import random
# Generate a random list of numbers between 1 and 10
random_numbers = [random.randint(1, 10) for _ in range(15)] # Generate 15 random numbers

# Convert the list to a set to remove duplicates
unique_numbers = set(random_numbers)

# Display the original list and unique numbers
print("Original list of numbers:", random_numbers)
print("Unique numbers (duplicates removed):", unique_numbers)

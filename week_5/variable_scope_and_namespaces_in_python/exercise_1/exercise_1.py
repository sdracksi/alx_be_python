# Define a global variable
message = "Global scope message"

def print_message():
    # Define a local variable with the same name
    message = "Local scope message"
    print("Inside the function:", message)  # Access the local variable

# Call the function
print_message()

# Print the global variable
print("Outside the function:", message)  # Access the global variable
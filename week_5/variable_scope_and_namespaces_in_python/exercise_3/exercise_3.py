# Global scope variable
name = "Global Name"

def outer_function():
    # Enclosing scope variable
    name = "Enclosing Name"
    
    def inner_function():
        # Local scope variable
        name = "Local Name"
        
        # Access the Local variable
        print("Inside inner_function - Local:", name)
        
        # Access the Enclosing variable using the nonlocal keyword
        nonlocal name
        print("Inside inner_function - Enclosing:", name)
        
        # Access the Global variable using the global keyword
        global name
        print("Inside inner_function - Global:", name)
    
    # Call the inner function
    inner_function()

# Call the outer function
outer_function()

# Print the global variable
print("Outside all functions - Global:", name)
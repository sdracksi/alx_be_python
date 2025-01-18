def counting_function():
    # Define a variable specific to this function
    count = 10
    print("Inside counting_function, count:", count)

def logging_function():
    # Define a variable with the same name but different purpose
    count = "Logging count variable"
    print("Inside logging_function, count:", count)

# Call both functions
counting_function()
logging_function()
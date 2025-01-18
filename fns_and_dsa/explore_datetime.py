from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculate a future date based on the user's input of days to add.
    """
    try:
        # Prompt the user to enter a number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate the future date
        future_date = datetime.now() + timedelta(days=days_to_add)
        
        # Format the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        # Print the future date
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input! Please enter an integer.")

def main():
    """
    Main function to execute the datetime operations.
    """
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display a future date
    calculate_future_date()

if __name__ == "__main__":
    main()
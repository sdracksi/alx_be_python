def main():
    # Prompt user for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process the task based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high-priority task"
        case "medium":
            reminder = f"'{task}' is a medium-priority task"
        case "low":
            reminder = f"'{task}' is a low-priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

    # Add time sensitivity to the reminder
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        return

    # Print the customized reminder
    print(f"Reminder: {reminder}")

if __name__ == "__main__":
    main()
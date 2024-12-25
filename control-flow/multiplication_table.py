def main():
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table
        for index in range(1, 11):
            product = number * index
            print(f"{number} * {index} = {product}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
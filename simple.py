# Simple Python program to print a greeting message

def greet(name):
    """Prints a greeting message with the given name."""
    print(f"Hello, {name}!")

# Main function
def main():
    # Prompt the user for their name
    user_name = input("Enter your name: ")
    # Call the greet function with the user's name
    greet(user_name)

# Entry point of the program
if __name__ == "__main__":
    main()

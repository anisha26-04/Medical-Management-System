from user import User

def user_menu():
    """Display user menu and handle actions."""
    user = User()  # Create an instance of User
    while True:
        print("\n--- User Menu ---")
        print("1. View Medicines")
        print("2. Purchase Medicine")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            user.display_medicines()
        elif choice == "2":
            user.purchase_medicine()
        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


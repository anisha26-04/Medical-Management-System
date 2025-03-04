from admin import Admin
from user import User

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Login as Admin")
        print("2. Login as User")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            admin = Admin()
            if admin.login():  # Ensure successful login before accessing the menu
                admin.menu()
        elif choice == "2":
            try:
                print("Loading inventory from the admin file: medi.txt")
                user = User()  # Ensure User class is properly defined
                user.purchase_medicine()  # Start the user process
            except FileNotFoundError:
                print("Error: Inventory file 'medi.txt' not found. Please add medicines as Admin first.")
            except AttributeError:
                print("Error: User class or method 'purchase_medicine()' is not defined correctly.")
            except Exception as e:
                print(f"Unexpected error: {e}")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

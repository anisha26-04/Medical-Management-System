from inventory import Inventory  
from medicine import Medicine  

class Admin:  
    def __init__(self):  
        self.username = "admin"  # Predefined admin username  
        self.password = "kiki"  # Predefined admin password  
        self.inventory = None  # Initialize Inventory instance after login  

    def login(self):  
        """Handles admin login with 3 attempts."""  
        attempts = 3  
        while attempts > 0:  
            print("\n--- Admin Login ---")  
            input_username = input("Enter username: ")  
            input_password = input("Enter password: ")  

            if input_username == self.username and input_password == self.password:  
                print("Login successful! Welcome, Admin.")  
                self.inventory = Inventory()  # Initialize Inventory after successful login  
                return True  
            else:  
                attempts -= 1  
                print(f"Invalid credentials. You have {attempts} attempt(s) remaining.")  

        print("Too many failed login attempts. Exiting program.")  
        return False  

    def menu(self):  
        """Display admin menu and perform actions."""  
        if self.inventory is None:  # Ensure inventory is initialized  
            print("Error: Inventory not initialized. Please log in first.")  
            return  

        while True:  
            print("\n--- Admin Menu ---")  
            print("1. Add Medicines")  
            print("2. Load Medicines")  
            print("3. Display Medicines")  
            print("4. Update Medicines")  
            print("5. Check Expired Medicines")  
            print("6. Delete Expired Medicines")  
            print("7. Exit")  

            choice = input("Enter your choice (1-7): ")  

            if choice == "1":  
                self.inventory.add_medicines()  
            elif choice == "2":  
                self.inventory.load_medicines()  
            elif choice == "3":  
                self.inventory.display_medicines()  
            elif choice == "4":  
                self.inventory.update_medicines()  
            elif choice == "5":  
                self.inventory.check_expired_medicines()  
            elif choice == "6":  
                self.inventory.delete_expired_medicines()  
            elif choice == "7":  
                print("Exiting Admin Menu. Goodbye!")  
                break  
            else:  
                print("Invalid choice. Please try again.")  






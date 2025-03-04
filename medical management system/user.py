from prettytable import PrettyTable
from datetime import datetime
from inventory import Inventory

class User:
    def __init__(self):
        """Initialize user details and load inventory."""
        self.user_data_file = "user_data.txt"
        self.admin_file_name = "inventory.txt"  
        self.cart = []  # Store purchased items

        print(f"Loading inventory from: {self.admin_file_name}")
        self.inventory = Inventory()

        if not self.inventory.medicines:
            print(f"No valid medicines found in {self.admin_file_name}.")
            return

        self.name = input("Enter your name: ").strip().capitalize()
        self.prescription = self.get_prescription_info()
        self.doctor_name = input("Enter the doctor's name: ").strip().capitalize() if self.prescription else None

    def get_prescription_info(self):
        """Ask the user if they have a prescription."""
        while True:
            response = input("Do you have a doctor's prescription? (yes/no): ").strip().lower()
            if response in ["yes", "no"]:
                return response == "yes"
            print("Invalid input. Please enter 'yes' or 'no'.")

    def save_user_data(self):
        """Save user purchase data to a file."""
        with open(self.user_data_file, "a") as file:
            for medicine_name, quantity, total_price in self.cart:
                file.write(
                    f"User: {self.name}, Prescription: {self.prescription}, "
                    f"Doctor: {self.doctor_name or 'N/A'}, Medicine: {medicine_name}, Quantity: {quantity}, "
                    f"Total Price: {total_price}, Date: {datetime.now()}\n"
                )

    def display_medicines(self):
        """Display available medicines."""
        if not self.inventory.medicines:
            print("No medicines available.")
            return

        table = PrettyTable()
        table.field_names = ["Name", "Power", "Price", "Quantity", "Expiry Date"]
        for medicine in self.inventory.medicines:
            table.add_row([medicine.name, medicine.power, medicine.price, medicine.quantity, medicine.expiry_date])

        print("\nAvailable Medicines:")
        print(table)

    def get_valid_quantity(self):
        """Ensure quantity is a valid positive integer."""
        while True:
            try:
                quantity = int(input("Enter the quantity: ").strip())
                if quantity > 0:
                    return quantity
                print("Quantity must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def purchase_medicine(self):
        """Allow the user to purchase multiple medicines."""
        while True:
            self.display_medicines()
            medicine_name = input("Enter the medicine name (or 'done' to finish): ").strip().lower()
            if medicine_name == 'done':
                break

            if not medicine_name:
                print("Medicine name cannot be empty.")
                continue

            quantity = self.get_valid_quantity()

            for medicine in self.inventory.medicines:
                if medicine.name.lower() == medicine_name:
                    if medicine.power.lower() == "high" and not self.prescription:
                        print("High-power medicines require a doctor's prescription. Purchase denied.")
                        break

                    if medicine.quantity >= quantity:
                        total_price = medicine.price * quantity
                        medicine.quantity -= quantity
                        self.cart.append((medicine.name, quantity, total_price))
                        print(f"Added {quantity} units of '{medicine.name}' to your cart.")
                    else:
                        print(f"Only {medicine.quantity} units of '{medicine.name}' are available.")
                    break
            else:
                print(f"Medicine '{medicine_name}' not found.")

        if self.cart:
            self.generate_bill()
            self.save_user_data()
            self.inventory.save_all_medicines()  # Update inventory

    def generate_bill(self):
        """Generate and display a detailed bill."""
        print("\n--- Bill Details ---")
        table = PrettyTable()
        table.field_names = ["Medicine Name", "Quantity", "Total Price"]
        grand_total = sum(total_price for _, _, total_price in self.cart)

        for medicine_name, quantity, total_price in self.cart:
            table.add_row([medicine_name, quantity, total_price])

        print(table)
        print(f"Grand Total: {grand_total}")

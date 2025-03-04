from datetime import datetime
from prettytable import PrettyTable
from medicine import Medicine

class Inventory:
    def __init__(self):
        """
        Initializes the Inventory instance with a file for storing medicines.
        """
        self.file_name = "inventory.txt"
        self.medicines = []  # List to store medicine objects
        self._initialize_file()
        self.load_medicines()

    def _initialize_file(self):
        """Ensures the inventory file exists."""
        try:
            open(self.file_name, "x").close()
        except FileExistsError:
            pass

    def add_medicines(self):
        """Adds a new medicine with input validation."""
        name = input("Enter medicine name: ").strip()
        if any(med.name.lower() == name.lower() for med in self.medicines):
            print("Medicine already exists. Use the update option.")
            return

        power = self._validate_power()
        price = self._validate_positive_int("Enter price: ")
        quantity = self._validate_positive_int("Enter quantity: ")
        expiry_date = self._validate_expiry_date()

        new_medicine = Medicine(name, power, price, quantity, expiry_date)
        self.medicines.append(new_medicine)
        self.save_all_medicines()
        print("Medicine added successfully.")

    def _validate_power(self):
        """Validates power input."""
        while True:
            power = input("Enter medicine power (High, Medium, Low): ").strip().capitalize()
            if power in ["High", "Medium", "Low"]:
                return power
            print("Invalid input. Choose from High, Medium, or Low.")

    def _validate_positive_int(self, prompt):
        """Ensures input is a positive integer."""
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                print("Value must be positive.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def _validate_expiry_date(self):
        """Validates expiry date format and future date."""
        while True:
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ").strip()
            try:
                date_obj = datetime.strptime(expiry_date, "%Y-%m-%d").date()
                if date_obj > datetime.now().date():
                    return expiry_date
                print("Expiry date must be in the future.")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

    def load_medicines(self):
        """Loads medicines from the file."""
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    try:
                        name, power, price, quantity, expiry_date = line.strip().split(",")
                        if not any(med.name.lower() == name.lower() for med in self.medicines):
                            self.medicines.append(Medicine(name, power, int(price), int(quantity), expiry_date))
                    except ValueError:
                        continue  # Skip invalid lines
        except FileNotFoundError:
            pass

    def save_all_medicines(self):
        """Saves all medicines to the file."""
        with open(self.file_name, "w") as file:
            for med in self.medicines:
                file.write(f"{med.name},{med.power},{med.price},{med.quantity},{med.expiry_date}\n")

    def display_medicines(self):
        """Displays all medicines in a table format."""
        if not self.medicines:
            print("No medicines available.")
            return

        table = PrettyTable(["Name", "Power", "Price", "Quantity", "Expiry Date"])
        for med in self.medicines:
            table.add_row([med.name, med.power, med.price, med.quantity, med.expiry_date])
        print(table)

    def update_medicines(self):
        """Updates medicine details."""
        name = input("Enter medicine name to update: ").strip()
        for medicine in self.medicines:
            if medicine.name.lower() == name.lower():
                print("1. Price\n2. Quantity\n3. Expiry Date")
                choice = input("Choose an option: ").strip()
                if choice == "1":
                    medicine.price = self._validate_positive_int("Enter new price: ")
                elif choice == "2":
                    medicine.quantity = self._validate_positive_int("Enter new quantity: ")
                elif choice == "3":
                    medicine.expiry_date = self._validate_expiry_date()
                else:
                    print("Invalid choice.")
                    return
                self.save_all_medicines()
                print("Medicine updated successfully.")
                return
        print("Medicine not found.")

    def check_expired_medicines(self):
        """Displays expired medicines."""
        current_date = datetime.now().date()
        expired_meds = [med for med in self.medicines if datetime.strptime(med.expiry_date, "%Y-%m-%d").date() < current_date]
        if not expired_meds:
            print("No expired medicines.")
            return
        table = PrettyTable(["Name", "Power", "Price", "Quantity", "Expiry Date"])
        for med in expired_meds:
            table.add_row([med.name, med.power, med.price, med.quantity, med.expiry_date])
        print("\nExpired Medicines:")
        print(table)

    def delete_expired_medicines(self):
        """Deletes expired medicines."""
        current_date = datetime.now().date()
        self.medicines = [med for med in self.medicines if datetime.strptime(med.expiry_date, "%Y-%m-%d").date() >= current_date]
        self.save_all_medicines()
        print("Expired medicines deleted.")

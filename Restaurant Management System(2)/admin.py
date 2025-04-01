class Admin:
    def __init__(self):
        self.menu = {}  # Stores menu items as {item_name: price}
        self.customers = {}  # Stores customers as {email: {name, address}}

    def add_menu_item(self, item_name, price):
        """Adds an item to the menu."""
        self.menu[item_name] = price
        print(f"Added {item_name} for {price}.")

    def remove_menu_item(self, item_name):
        """Removes an item from the menu."""
        if item_name in self.menu:
            del self.menu[item_name]
            print(f"Removed {item_name} from the menu.")
        else:
            print(f"Item {item_name} not found.")

    def update_menu_item(self, item_name, new_price):
        """Updates the price of an item."""
        if item_name in self.menu:
            self.menu[item_name] = new_price
            print(f"Updated {item_name} to {new_price}.")
        else:
            print(f"Item {item_name} not found.")

    def add_customer(self, name, email, address):
        """Adds a new customer."""
        if email not in self.customers:
            self.customers[email] = {"name": name, "address": address}
            print(f"Customer {name} added.")
        else:
            print("Customer already exists.")

    def view_customers(self):
        """Displays all registered customers."""
        if self.customers:
            for email, info in self.customers.items():
                print(f"{info['name']} ({email}) - {info['address']}")
        else:
            print("No customers found.")

    def remove_customer(self, email):
        """Removes a customer account."""
        if email in self.customers:
            del self.customers[email]
            print(f"Customer {email} removed.")
        else:
            print("Customer not found.")

    def view_menu(self):
        """Displays the menu."""
        if self.menu:
            for item, price in self.menu.items():
                print(f"{item}: ${price}")
        else:
            print("Menu is empty.")

# Example usage:
admin = Admin()
admin.add_menu_item("Pizza", 12.99)
admin.add_menu_item("Burger", 5.99)
admin.view_menu()
admin.update_menu_item("Burger", 6.49)
admin.remove_menu_item("Pizza")
admin.view_menu()
admin.add_customer("John Doe", "john@example.com", "123 Street")
admin.view_customers()
admin.remove_customer("john@example.com")
admin.view_customers()

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}  # Stores menu items as {item_name: price}
        self.customers = {}  # Stores customers as {email: {name, address}}

    def add_menu_item(self, item_name, price):
        """Adds an item to the menu."""
        self.menu[item_name] = price
        print(f"{item_name} added to the menu at ${price}.")

    def remove_menu_item(self, item_name):
        """Removes an item from the menu."""
        if item_name in self.menu:
            del self.menu[item_name]
            print(f"{item_name} removed from the menu.")
        else:
            print(f"{item_name} not found in the menu.")

    def show_menu(self):
        """Displays the restaurant menu."""
        if self.menu:
            print(f"\n{self.name} Menu:")
            for item, price in self.menu.items():
                print(f"{item}: ${price}")
        else:
            print("The menu is empty.")
    
    def add_customer(self, name, email, address):
        """Adds a new customer."""
        if email not in self.customers:
            self.customers[email] = {"name": name, "address": address}
            print(f"Customer {name} added.")
        else:
            print("Customer already exists.")
    
    def remove_customer(self, email):
        """Removes a customer."""
        if email in self.customers:
            del self.customers[email]
            print(f"Customer {email} removed.")
        else:
            print("Customer not found.")
    
    def show_customers(self):
        """Displays all registered customers."""
        if self.customers:
            print("\nRegistered Customers:")
            for email, info in self.customers.items():
                print(f"{info['name']} ({email}) - {info['address']}")
        else:
            print("No customers found.")

# Example usage:
restaurant = Restaurant("Tasty Bites")
restaurant.add_menu_item("Pasta", 8.99)
restaurant.add_menu_item("Salad", 4.99)
restaurant.show_menu()
restaurant.add_customer("Alice", "alice@example.com", "456 Avenue")
restaurant.show_customers()
restaurant.remove_menu_item("Pasta")
restaurant.remove_customer("alice@example.com")
restaurant.show_menu()
restaurant.show_customers()

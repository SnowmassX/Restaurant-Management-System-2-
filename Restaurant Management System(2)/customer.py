class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.menu = {
            'Pizza': 10,
            'Burger': 5,
            'Pasta': 7,
            'Soda': 2,
            'Coffee': 3
        }
        self.orders = []
    
    def view_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")
    
    def check_balance(self):
        print(f"Available balance: ${self.balance}")
    
    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added ${amount} to balance. New balance: ${self.balance}")
        else:
            print("Amount must be positive!")
    
    def place_order(self, *items):
        total_cost = sum(self.menu[item] for item in items if item in self.menu)
        if total_cost == 0:
            print("Invalid items selected!")
            return
        
        if self.balance >= total_cost:
            self.balance -= total_cost
            self.orders.append(items)
            print(f"Order placed: {', '.join(items)} for ${total_cost}")
            print(f"Remaining balance: ${self.balance}")
        else:
            print("Insufficient balance! Please add funds.")
    
    def view_past_orders(self):
        if not self.orders:
            print("No past orders.")
        else:
            print("Past Orders:")
            for i, order in enumerate(self.orders, 1):
                print(f"{i}. {', '.join(order)}")

# Example usage:
cust = Customer("John", 20)
cust.view_menu()
cust.check_balance()
cust.place_order("Pizza", "Soda")
cust.view_past_orders()
cust.add_funds(10)
cust.place_order("Burger", "Coffee")

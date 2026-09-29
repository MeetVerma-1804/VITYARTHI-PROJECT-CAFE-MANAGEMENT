# CAFE MANAGEMENT 
menu = {
    1: {"name": "Coffee", "price": 80},
    2: {"name": "Cappuccino", "price": 120},
    3: {"name": "Cold Coffee", "price": 140},
    4: {"name": "Tea", "price": 50},
    5: {"name": "Veg Sandwich", "price": 100},
    6: {"name": "Cheese Burger", "price": 110},
    7: {"name": "French Fries", "price": 90},
    8: {"name": "Pizza", "price": 240},
    9: {"name": "Brownie", "price": 120},
    10: {"name": "Chocolate Cake", "price": 150},
}

cart = {} # To store selected items with its name and price

def view_menu():
    #Display the cafe menu
    print("\n")
    print("=" * 42)
    print("         CAFE MENU")
    print("=" * 42)
    for i, item in menu.items():
        print(f"{i}. {item['name']:<20} Rs {item['price']}")



def add_item():
# Display the menu before taking the order
    view_menu()
# Take item number and quantity from the customer 
    item_input = input("Enter item number: ").strip()
    quantity_input = input("Enter quantity: ").strip()

# Check whether both inputs contain numbers only
    if not item_input.isdigit() or not quantity_input.isdigit():
        print("Please enter numbers only")
        return

# Convert the input value from striing to integer
    item = int(item_input)
    quantity = int(quantity_input)

# Check whetehr the entered item number exists in the menu
    if item not in menu:
        print("Invalid Item Number")

    elif quantity <= 0:
        print("Invalid Quantity")

    else:
        cart[item] = cart.get(item, 0) + quantity
        print("Item added to cart successfully")


def view_cart():
# Display which items are inside the cart

# Check if the cart is empty
    if not cart:
        print(" Cart is Empty ")
        return

    print("\n")
    print("=" * 50)
    print("         YOUR CART")
    print("=" * 50)

# Initialize the bill amount to 0
    total = 0

    for item, quantity in cart.items():
    # Get the item name and price from the menu
        name = menu[item]["name"]
        price = menu[item]["price"]
        amount = price * quantity # Calculate the total cost for the specific item 
        total += amount # Add the item's cost to the total bill

        print(f"{name:<20} x {quantity} = Rs{amount}")

    print("-" * 50)
    print(f"Total: Rs{total}") # Print the final total bill at the end


def remove_item():
# To remove item that are already present in the cart 

    if not cart:
        print(" Cart is empty ")
        return

    item_input = input("Enter Item number to Removed:").strip()

    if item_input.isdigit():
        item = int(item_input)

# Check if the item exists in the cart
        if item in cart:
            del cart[item] # Remover item from the cart
            print("Item removed Successfully")

        else:
            print("Item not Found")

    else: # If the user inputs any letter or special caharacter
        print("Enter valid number to Remove")


def clear_cart():
# To remove all present item from the cart at once

    cart.clear()
    print("Cart cleared Successfully")


def bill_generation():

    if not cart:
        print(" Cart is Empty ")
        return

# Calculate the initial total price of all items in the cart 
    total = sum(menu[i]["price"] * quantity for i, quantity in cart.items())
    gst = total * 0.05 # To calculate 5% gst on the food

# To calculate 10% discount on order above rs 1000
    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0

    grand_total = total + gst - discount # Calculate the final amount to be paid 

    print("\n")
    print("=" * 42)
    print("         Bill")
    print("=" * 42)

    for item, qty in cart.items():
        name = menu[item]["name"]
        price = menu[item]["price"]
    # Print the item name, quantity and total price to be paid
        print(f"{name:<20} x {qty} = ₹{price * qty:.2f}")

    print("-" * 42)

    print(f"total : ₹{total:.2f}") # prints the total of the items in the cart upto 2 decimal places
    print(f"GST (5%) : ₹{gst:.2f}")
    print(f"Discount : ₹{discount:.2f}")
    print(f"TOTAL    : ₹{grand_total:.2f}") # prints the grand total amount to be paid after adding gst and subtracting discount
    print("================================")
    print("Thank you! Visit again!")

    cart.clear() # Empties the cart completely to prepare for the next order

# MAIN MENU OF CAFE
while True:
    print("\n")
    print("=" * 42)
    print("         BISTRO BY SAFAL")
    print("=" * 42)
    print("\n")
# To display the available options in ther menu
    print("1. View Menu")
    print("2. Add Item ")
    print("3. View Cart")
    print("4. Remove Item")
    print("5. Clear Cart")
    print("6. Place Order and Generate Bill")
    print("7. Exit")

    print("-" * 42)
    
    c = int(input("Enter your Choice: ")) # Take user input for options

    if c == 1:
        view_menu()
    elif c == 2:
        add_item()
    elif c == 3:
        view_cart()
    elif c == 4:
        remove_item()
    elif c == 5:
        clear_cart()
    elif c == 6:
        bill_generation()
    elif c == 7:
        print("Thankyou for Visiting")
        break
    else:
        print("Invalid Choice")

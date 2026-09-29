# Cafe Management System

## Project Title

Bistro by Safal -- Cafe Management System

## Overview of the Project

A simple console based

Cafe Management System made in

the python programming language. This project allows the customer to view the entire cafe menu, add items to a cart, view the cart details, remove an item, clear cart, and place the order.
The application also calculates the item total and 5% GST, and provides a 10% discount on orders of Rs 1000 or more. After generating the bill, the cart is cleared so the next order can be placed.
## Features
-  View the complete list of cafe items and their prices.

-  Add items to the cart by specifying the item number and quantity.
-  View the list of items in the cart.
-  Calculate the total cost of items in the cart.
-  Remove an item from the cart.
-  Clear all items from the cart.
-  Generate the final bill.
-  Calculate 5% GST on the order.
-  Apply a 10% discount if the order is of Rs 1000 or more.
-  Clear the cart once the bill has been generated.
-  Exit the application from the main menu.
## Menu Items
No.  Item        Price
----- ---------------- --------
1   Coffee       Rs 80
2   Cappuccino     Rs 120
3   Cold Coffee    Rs 140
4   Tea         Rs 50
5   Veg Sandwich    Rs 100
6   Cheese Burger   Rs 110
7   French Fries    Rs 90
8   Pizza       Rs 240
9   Brownie      Rs 120
10  Chocolate Cake   Rs 150
## Technologies/Tools Used
-  Python
-  Python dictionaries to store the menu and cart data
-  Python functions for various cafe related operations
-  Console/terminal for interaction

## Project Structure

``` text

Cafe-Management/
│
├── main.py
└── README.md
```

## Steps to Install & Run the Project
### 1. Install Python
Make sure that Python is correctly installed on your system.
You can test this by executing the following command in the terminal:
``` bash
python --version
```
### 2. Download or Clone the Repository
Now, clone the GitHub repository:
``` bash
git clone
```
Enter the project directory:
``` bash
cd Cafe-Management
```
### 3. Run the Program
Run the Python file:
``` bash
python main.py
```
The BISTRO BY SAFAL main menu will be displayed in the terminal.
## Instructions for Testing
After running the program, test the following from the main menu:
1. View Menu -- Check if all the cafe items and prices are displayed correctly.
2. Add Item -- Enter a valid item number and quantity and check if the item is added successfully.
3. View Cart -- Check if all the selected items, quantity, and the amount are displayed.
4. Remove Item -- Enter an item number which is present in the cart and check if the item is removed.
5. Clear Cart -- Check if all items are removed from the cart.
6. Place Order and Generate Bill -- Add items and generate a bill. Check if the item total, GST, discount, and total amount are displayed.
7. Discount Testing -- Test placing an order with a total of Rs 1000 or more to check if 10% discount is applied on the order.
8. Exit -- Select option 7 and check if the program exits.
### Input Validation Testing
You can also test invalid inputs, if any, like:
-  Entering letters instead of numbers for item number or quantity
-  Entering item number which does not exist
-  Entering zero or a negative quantity
-  Trying to remove an item which is not present in the cart
-  Trying to view or generate a bill when the cart is empty
## Screenshots
The screenshots of the running application can be added here after testing the project.
Example:
``` text
![Cafe Menu Screenshot](screenshots/menu.png)
![Cart Screenshot](screenshots/cart.png)
![Bill Screenshot](screenshots/bill.png)
```
## Conclusion
The Bistro by Safal Cafe Management System demonstrates the implementation of basic python concepts like dictionaries, functions, loops, conditional statements, and calculations of the order amount and GST. This project provides a simple command-line interface to manage orders of the cafe. The application also demonstrates the practical implementation of GST calculation and conditional discounts.
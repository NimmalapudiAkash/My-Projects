# Define the menu of the restaurant
menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

# Greet the customer
print("Welcome to PYTHON Restaurant")
print("Menu:\nPizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

order_total = 0
ordered_items = []


item_1 = input("Enter the name of the item you want to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    ordered_items.append((item_1.capitalize(), menu[item_1]))  
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, the item '{item_1}' is not available!")

# Ask if the customer wants to add another item
another_order = input("Do you want to add another item? (Yes/No): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        ordered_items.append((item_2.capitalize(), menu[item_2])) 
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, the item '{item_2}' is not available!")

# Display the ordered items and total amount
print("\nYour order summary:")
if ordered_items:
    for item, price in ordered_items:
        print(f"{item}: Rs{price}")
else:
    print("No items ordered.")

print(f"The total amount to pay is Rs{order_total}.")

# Coffee Machine Project

This is a simple coffee machine simulation built with Python. The coffee machine offers three types of coffee: `latte`, `espresso`, and `cappuccino`. The user can insert coins, and the machine will prepare the coffee if there are enough resources available.

## Features
- **Coffee Menu**: Choose from `latte`, `espresso`, or `cappuccino`.
- **Resource Management**: The machine keeps track of available water, milk, and coffee.
- **Coin Processing**: The machine accepts coins in denominations of 5, 10, and 20 rupees.
- **Reports**: View the current resource levels and profits.
- **Turn Off**: The machine can be turned off by the user.

## How to Use
1. Clone the repository:
    ```bash
    git clone https://github.com/NimmalapudiAkash/My-Projects/blob/main/coffee%20manchine/co.py
    cd coffee-machine
    ```

2. Run the script:
    ```bash
    python coffee_machine.py
    ```

3. The machine will prompt you to select a drink:
    ```
    what would you like to have? (latte/espresso/cappuccino): 
    ```

4. Insert coins when prompted:
    ```
    please insert coins.
    How many 5rs coin?: 
    How many 10rs coin?: 
    How many 20rs coin?: 
    ```

5. If enough resources and coins are available, your coffee will be served.

## Example

```bash
what would you like to have? (latte/espresso/cappuccino): latte
please insert coins.
How many 5rs coin?: 1
How many 10rs coin?: 3
How many 20rs coin?: 2





# PYTHON Restaurant Ordering System

This is a simple Python program that simulates an ordering system for a restaurant. The program takes customer orders from a pre-defined menu and calculates the total amount. The customer can add one or two items to their order.

## Menu
- Pizza: Rs40
- Pasta: Rs50
- Burger: Rs60
- Salad: Rs70
- Coffee: Rs80

## How It Works
1. The program displays the menu to the customer.
2. The customer is asked to input the name of the item they want to order.
3. If the item is available, it will be added to the order.
4. The customer is then asked if they would like to add a second item.
5. After the second item is ordered (or if they decline), the program displays a summary of the order and the total cost.

## Sample Usage

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/restaurant-ordering-system.git
    ```
2. Navigate to the directory:
    ```bash
    cd restaurant-ordering-system
    ```
3. Run the Python script:
    ```bash
    python restaurant_order.py
    ```

## Requirements
This is a simple script that runs with Python 3.x. No additional libraries are required.

## Future Enhancements
- Add more items to the menu.
- Allow customers to order more than two items.
- Include an option for customers to remove items from their order.
- Implement a graphical user interface (GUI) for a more user-friendly experience.

## License
This project is licensed under the MIT License.


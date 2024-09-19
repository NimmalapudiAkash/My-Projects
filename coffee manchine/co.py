# coffee-manchine
from importlib import resources


Menu={
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffe": 24,
        },
        "cost":150
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    }
}
profit=0
resource ={
    "water": 500,
    "milk": 200,
    "coffe": 100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("please insert coins.")
    total=0
    coins_five=int(input("How many 5rs coin?: "))
    coins_ten=int(input("How many 10rs coin?: "))
    coins_twenty=int(input("How many 20rs coin?: "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return total
is_on=True
while is_on:
    choice=input("what would you like to have? (latte/espresso/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resource['water']}ml")
        print(f"milk={resource['milk']}ml")
        print(f"coffee={resource['coffee']}g")
        print(f"money=Rs{profit}")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)

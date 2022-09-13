MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    """Return True when the ingrediants are available"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Return the total calculated from coins inserted"""
    print("Please insert coins: ")
    total = int(input("How many quarters: ")) * 0.25
    total = int(input("How many dimes: ")) * 0.1
    total = int(input("How many nickles: ")) * 0.05
    total = int(input("How many pennies: ")) * 0.01
    return total

def is_transaction_successful(money_received, drint_cost):
    """Return True when money is received and False when money is insufficient."""
    if money_received >= drint_cost:
        change = round(money_received - drint_cost, 2)
        print(f"Here is ${change} in change ")
        profit += drint_cost
        return True
    else:
        print("“Sorry that's not enough money. Money refunded.")
        return False


machine_on_off =  True
while machine_on_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ") 
    if choice == "off":
        machine_on_off = False
    elif choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:$ {profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingrediants"]):
            payment = process_coins()
            




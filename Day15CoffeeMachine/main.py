# Coffee Machine Project

# Menu Dictionary

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00
}


# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.

def turn_off():
    print("Turning off...")
    return


# TODO 3. Print report.

def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")


# TODO 4. Check resources sufficient?

def check_resources(order):
    resources_sufficient = True
    print("Checking resources...")
    for key in resources:
        print(f"{key}: {resources[key]}")
        if key == "water":
            if resources[key] < MENU[order]["ingredients"]["water"]:
                print("Sorry, there is not enough water.")
                resources_sufficient = False
            else:
                resources[key] -= MENU[order]["ingredients"]["water"]
                print(f"Water: {resources[key]}")
        elif key == "milk":
            if order == "espresso":
                continue
            elif resources[key] < MENU[order]["ingredients"]["milk"]:
                print("Sorry, there is not enough milk.")
                resources_sufficient = False
            else:
                resources[key] -= MENU[order]["ingredients"]["milk"]
                print(f"Milk: {resources[key]}")
        elif key == "coffee":
            if resources[key] < MENU[order]["ingredients"]["coffee"]:
                print("Sorry, there is not enough coffee.")
                resources_sufficient = False
            else:
                resources[key] -= MENU[order]["ingredients"]["coffee"]
                print(f"Coffee: {resources[key]}")
    return resources_sufficient


# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.
def process_coins(order):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if total < MENU[order]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        change = total - MENU[order]["cost"]
        print(f"Here is ${round(change, 2)} in change.")
        resources["money"] += MENU[order]["cost"]
        print(f"Here is your {order} ☕️. Enjoy!")


still_open = True
# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while still_open:
    customer_order = input("What would you like? (espresso/latte/cappuccino): ")

    if customer_order == "off":
        still_open = False
        turn_off()
    elif customer_order == "report":
        print_report()
    elif customer_order == "espresso" or customer_order == "latte" or customer_order == "cappuccino":
        if not check_resources(customer_order):
            print("Sorry, there is not enough resources.")
        else:
            process_coins(customer_order)
    else:
        print("Error: Invalid order")
        exit()
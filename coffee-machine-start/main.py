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
}

# TODO 1: Ask user what they want. This prompt should show everytime after action is completed


def drink_selection():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


machine_on = True
total_money = 0.0


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = float(total_money)
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def check_resources(drink):
    current_drink = MENU[drink]
    enough_ingredients = True

    for ingredient in current_drink['ingredients']:
        if resources[ingredient] < current_drink['ingredients'][ingredient]:
            enough_ingredients = False
            break
    print(enough_ingredients)
    return enough_ingredients


def enter_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    sum_coins = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    print(sum_coins)
    return sum_coins


def update_report(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        print(ingredient)


def transaction(coins_input,drink):
    menu_drink_cost = MENU[drink]["cost"]
    cost_difference = menu_drink_cost-coins_input
    if cost_difference == 0:
        print("Update report")
    elif cost_difference > 0:
        print("Not enough funds")
    else:
        print("Here's money back")


while machine_on:
    user_input = drink_selection()

    # TODO 2: Turn off coffee machine by entering 'off' in prompt

    # TODO 3: Print Report - when user enters report in prompt, resources should be printed out
    if user_input == 'report':
        report()
    if user_input == 'off':
        machine_on = False

    # TODO 4: Check if resources are sufficient - are there enough resources to fulfill order?
    if check_resources(user_input):
        # TODO 5: Prompt user to enter coins
        # TODO 5A: calculate value of coins inserted
        total_input = enter_coins()
        # TODO 6: Was transaction successful? Enough money inserted?
        transaction(total_input, user_input)
        #TODO 6A: If enough money, cost of drink to make is deducated from resources and added to report

        #TODO 6B: If user inserted too much money, machine offers change
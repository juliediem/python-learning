from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_active = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while machine_active:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'off':
        machine_active = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        menu.get_items()
        selected_item = menu.find_drink(user_input)
        sufficient_resources = coffee_maker.is_resource_sufficient(selected_item)
        if sufficient_resources:
            money_machine.make_payment(selected_item.cost)
            coffee_maker.make_coffee(selected_item)







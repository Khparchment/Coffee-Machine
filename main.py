from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    drink_options = menu.get_items()
    drink_choice = input(f"What would you like? {drink_options} ")
    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(order):
            money_machine.make_payment(order.cost)
            coffee_maker.make_coffee(order)



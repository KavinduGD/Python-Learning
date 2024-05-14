from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    key_word = input('What would you like? (espresso/latte/cappuccino): ')
    type = ""
    if key_word == "espresso" or key_word == "latte" or key_word == "cappuccino":
        type = key_word
        menu_item = menu.find_drink(type)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)

    if key_word == "off":
        break
    if key_word == "report":
        coffee_maker.report()
        money_machine.report()

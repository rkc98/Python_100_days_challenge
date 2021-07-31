from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
# menuitems=MenuItem()
coffeemaker=CoffeeMaker()
moneymachine=MoneyMachine()

coffeemaker.report()
moneymachine.report()
# user_choice=input("what would you like to have? (espresso,latte,cappuccino):")
# menu.get_items()
# coffeemaker.is_resource_sufficient(user_choice)

start_machine=True

while start_machine:
    options=menu.get_items()
    user_choice=input(f"what would you like to have? {options}:")
    if user_choice=="off":
        start_machine=False
    elif user_choice=="report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink=menu.find_drink(user_choice)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
            else:
                start_machine=False
        else:
            start_machine=False
        





        








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
    "water": 1000,
    "milk": 500,
    "coffee": 100,
}
report_list = {
    "water": resources["water"],
    "milk": resources["milk"],
    "coffee": resources["coffee"],
    "money": 0
}


def report():
    print(
        f" water: {report_list['water']} \n milk: {report_list['milk']} \n coffee: {report_list['coffee']} \n money: {report_list['money']}")


def check_resources(require):
    temp = 0
    for items in MENU[require]["ingredients"]:
        if MENU[require]["ingredients"][items] < report_list[items]:
            temp += 0
        else:
            temp += 1
    if temp > 0:
        return False
    else:
        return True


def process_coins(choice):
    quaters = int(input("enter the number of quaters: "))
    dimes = int(input("enter the number of dimes: "))
    nickel = int(input("enter the number of nickel: "))
    pennies = int(input("enter the number of pennies: "))

    total = (quaters*0.25)+(dimes*0.10)+(nickel*0.05)+(pennies*0.01)
    if total > MENU[choice]["cost"]:
        return round(total-MENU[choice]["cost"],2)
    else:
        return None


def make_a_coffe(choice):
    for items in MENU[choice]["ingredients"]:
        report_list[items] = report_list[items] - \
            MENU[choice]["ingredients"][items]
    report_list["money"] += MENU[choice]["cost"]


game_start = True
while game_start:
    user_input = input(
        "what would you like to have? (espresso,latte,cappuccino):")
    if(user_input == "report"):
        report()
    elif(user_input == "espresso"):
        available = check_resources(user_input)
        if available:
            funds = process_coins(user_input)
            if funds != None:
                make_a_coffe(user_input)
                print(f"here is your {user_input} please enjoy!!!!")
            else:
                print("insufficient money")
                break
        else:
            print("resources not available")
            break
    elif(user_input == "latte"):
        available = check_resources(user_input)
        if available:
            funds = process_coins(user_input)
            if funds != None:
                make_a_coffe(user_input)
                print(f"here is your {user_input} please enjoy!!!!")
            else:
                print("insufficient money")
                break
        else:
            print("resources not available")
            break
    elif(user_input == "cappuccino"):
        available = check_resources(user_input)
        if available:
            funds = process_coins(user_input)
            if funds != None:
                make_a_coffe(user_input)
                print(f"here is your {user_input} please enjoy!!!!")
                print(f"here is you left over change: {funds}")
            else:
                print("insufficient money")
                break
        else:
            print("resources not available")
            break
    elif(user_input == "off"):
        print("machine has been turned off")
        break
    else:
        print("please check your input")
        break

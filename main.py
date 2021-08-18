

MACHINE_IS_ON = True
MONEY_IN = 0


coins = {
    "penny"  : 0.01,
    "dime" : 0.10,
    "nickel" : 0.05,
    "quarter" : 0.25
}



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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



# TODO: 2. Check resourses sufficient?


#def check_resources(resources,drink_requested):
  #  if resources["water"] < MENU[drink_requested]["ingredients"]["water"] or resources["milk"] < MENU[drink_requested]["ingredients"]["milk"] or resources["coffee"] < MENU[drink_requested]["ingredients"]["coffee"]:
  #      print("sorry not enough resources, plesae refill the missing ingredients")
    #    return False
 #   else:
#       return True

def check_resources(resources,drink_requested):
    for item in resources:
        if resources[item] < MENU[drink_requested]["ingredients"][item]:
            print(f"sorry not enough {item}, please refill it")
            return  False
        else:
            return True

# TODO: 3. Print report of the coffe machine resources

def update_resources(resources,drink_requested):
    '''takes in the initial resources and the requested drink,updates quantity and print the resources left'''
    resources["water"] -= MENU[drink_requested]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink_requested]["ingredients"]["coffee"]
    resources["milk"] -= MENU[drink_requested]["ingredients"]["milk"]
    water_left = resources["water"]
    coffee_left = resources["coffee"]
    milk_left = resources["milk"]
    return  resources
  #  print(f" There are still {water_left} ml of water , {coffee_left} gr of coffe and ,{milk_left} ml of milk left")

def show_resources():
    water_left = resources["water"]
    coffee_left = resources["coffee"]
    milk_left = resources["milk"]
    print(f" There are still {water_left} ml of water , {coffee_left} gr of coffe and ,{milk_left} ml of milk left")

def process_payment(coins_inserted, drink_price):
    change = float(coins_inserted - drink_price )
    if change == 0:
        return  True
    elif change > 0:
        print(f"Here is $ {change} in change.")
        return  True
    else:
        change = -change
        print(f"Not enough coins inserted, please insert {change} $")
        MACHINE_IS_ON = False
        return  False




# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while MACHINE_IS_ON:

    drink_requested = str(input("What would you like? (espresso/latte/cappuccino):"))
    if drink_requested == "off":
        MACHINE_IS_ON = False
    elif drink_requested == "report":
        show_resources()
    else:
        if check_resources(resources, drink_requested):
            total_amount = 0
            drink_price = int(MENU[drink_requested]["cost"])
            print(f"pease insert {drink_price} $: ")
            quarters_total = float(coins["quarter"])  * int(input("How many quarters? "))
            print(f"inserted {quarters_total} $")
            dimes_total = float(coins["dime"])  * int(input("How many dimes? "))
            print(f"inserted {dimes_total + quarters_total} $")
            pennies_total = float(coins["penny"])  * int(input("How many pennies? "))
            print(f"inserted {pennies_total + dimes_total + quarters_total} $")
            nickels_total = float(coins["nickel"])  * int(input("How many nickels? "))
            print(f"inserted {nickels_total + pennies_total + dimes_total + quarters_total} $")
            total_amount = nickels_total + pennies_total + dimes_total + quarters_total

            coins_inserted = float(total_amount)
    # TODO: 7 Make coffe
            if process_payment(coins_inserted,drink_price):
                update_resources(resources,drink_requested)
                print(f"here is your {drink_requested}, enjoy!")





# TODO: 5. Process coins

# TODO: 6 Check transaction successful?


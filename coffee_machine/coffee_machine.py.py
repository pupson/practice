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



def order_tracker(order):

    order_lst = ['espresso', 'latte', 'cappuccino']
    espresso_count = 0
    latte_count = 0
    cappuccino_count = 0
    invalid_drink = False

    if order not in order_lst:
        """
        if order == 'espresso':
            espresso_count += 1
        elif order == 'latte':
            latte_count += 1
        elif order == 'cappuccino':
            cappuccino_count += 1
        """
        invalid_drink = True

    # return espresso_count, latte_count, cappuccino_count, invalid_drink
    return invalid_drink


# TODO: 3. Print report

def report():
    '''
    eg. return
    Water: 100 ml
    Milk: 50 ml
    Coffee: 76 g
    '''

    water_total = resources['water']
    milk_total = resources['milk']
    coffee_total = resources['coffee']

    print(f'Water: {water_total} ml\nMilk: {milk_total} ml\nCoffee: {coffee_total} g')


# TODO: 4. Check resources sufficient?

def update_resources(order):

    resource_lst = ['water', 'milk', 'coffee']

    stop = False

    for resource in resource_lst:
        if resources[resource] < MENU[order]['ingredients'][resource]:
            print(f'You do not have enough {resource}')
            stop = True
        else:
            resources[resource] =  resources[resource] - MENU[order]['ingredients'][resource]


    report()

    return stop

# TODO: 5. Process coins

def argent(price, profit):

    argent_dict = {'quarter': .25, 'dime': .10, 'nickel': .05, 'penny': .01}

    total = 0

    while total < price:

        quarters = int(input('How many quarters are you inserting? '))
        dimes = int(input('How many dimes are you inserting? '))
        nickels = int(input('How many nickels are you inserting? '))
        pennies = int(input('How many pennies are you inserting? '))

        total = (quarters * argent_dict['quarter']) + (dimes * argent_dict['dime']) + (nickels * argent_dict['nickel']) + (pennies * argent_dict['penny'])

        if total < price:
            print(f"That's not enough, you need to insert {round((price - total), 2)} more. Try again.")
        elif total > price:
            profit += round(price, 2)
            print(f"You paid too much, here is your change: {round((total - price), 2)}")
        else:
            profit += round(price, 2)
            print(f"You have paid {round(total, 2)}")

    return profit

def coffee_maker():

    power = True
    profit = 0

    while power:

        # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        order = input(f"What would you like? (espresso/latte/cappuccino): \n")

        invalid_drink = order_tracker(order)

        if invalid_drink:
            print('That is not a valid drink option. Try again.')
        else:
            price = MENU[order]['cost']
            print(f'That will be {price}\n')

            # TODO: 6. Check transaction successful?
            profit = argent(price, profit)

            # TODO: 7. Make Coffee.
            stop = update_resources(order)

            if stop:
                print('Sorry we do not have enough ingredients today.')
            else:
                print(f'Here is your {order}\n')
                print(f'The machine has profited {profit}')

                # espresso_count, latte_count, cappuccino_count, invalid_drink = order_tracker(order)

                # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
                power_status = input(f"Would you like another drink? yes/no ").lower()
                if power_status == "no":
                    power = False


coffee_maker()
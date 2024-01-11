print('    ____     _                             _         \n'
      '   / __ \   (_) ____ ____  ___    _____   (_)  ____ _\n'
      '  / /_/ /  / / /_  //_  / / _ \  / ___/  / /  / __ `/\n'
      ' / ____/  / /   / /_ / /_/  __/ / /     / /  / /_/ / \n'
      '/_/      /_/   /___//___/\___/ /_/     /_/   \__,_/ ')

print('--------------------------------')

money = float(input('Please enter a money amount: '))
total_money = 0
order = []

# Pizzas
PIZZA_HAWAINA: float = 27.648
PIZZA_SICILIANA: float = 37.400
FOUR_CHEESE_PIZZA: float = 38700

# Extra ingredients
EXTRA_CHEESE = 3000
EXTRA_MOZALERA = 2500
EXTRA_CHICKEN = 3200


def menu_order(money, total_money):
    while True:
        # Print Menu
        print(f'1- Pizza Hawaina {PIZZA_HAWAINA}$')
        print(f'2- Pizza Siciliana {PIZZA_SICILIANA}$')
        print(f'3- Four cheese pizza {FOUR_CHEESE_PIZZA}$ ')

        selected_pizza_order = int(input('Por favor ingrese la opcion'
                                         'que desea: '))

        match selected_pizza_order:
            case 1:
                print('Select the Pizza Hawaina.'
                      f'\ntotal payable {PIZZA_HAWAINA}$')
                money -= PIZZA_HAWAINA
                print(f'Fits you - {round(money, 2)}$.')
                total_money += PIZZA_HAWAINA
                order.append(f'Pizza Hawaina - {PIZZA_HAWAINA}$')
                break
            case 2:
                print('Select the Pizza Siciliana.'
                      f'\ntotal payable {PIZZA_SICILIANA}')
                money -= PIZZA_SICILIANA
                print(f'Fits you - {round(money, 2)}$')
                total_money += PIZZA_SICILIANA
                order.append(f'Pizza Siciliana - {PIZZA_SICILIANA}')
                break
            case 3:
                print('Select the Four Cheese Pizza.'
                      f'\ntotal payable {FOUR_CHEESE_PIZZA}')
                money -= FOUR_CHEESE_PIZZA
                print(f'Fits you - {round(money, 2)}$')
                total_money += FOUR_CHEESE_PIZZA
                order.append(f'Four Cheese Pizza - {FOUR_CHEESE_PIZZA}')
                break
            case _:
                print('Incorrect option, select one that is correct (1,2,3).')


menu_order(money, total_money)


def menu_extra_ingredients(money, total_money):
    print(f'1- Extra Cheese - {EXTRA_CHEESE}$')
    print(f'2- Extra Mozalera - {EXTRA_MOZALERA}$')
    print(f'3- Extra Chicken - {EXTRA_CHICKEN}$')
    print('4- Add nothing extra and pay.')

    option_extra_ingredient = input('Do you want to add extra ingredient: ')

    match option_extra_ingredient:
        case 1:
            print('You have selected extra cheese.'
                  f'\nExtra payable {EXTRA_CHEESE}$.')
            money -= EXTRA_CHEESE
            total_money += EXTRA_CHEESE
            print(f"Total payable: {total_money}$.")
            print(f"Fits you {round(money, 2)}$.")
            order.append(f"Extra Cheese - {EXTRA_CHEESE}$")
        case 2:
            print('You have selected extra mozarela.'
                  f'\nExtra payable {EXTRA_MOZALERA}$.')
            money -= EXTRA_MOZALERA
            total_money += EXTRA_MOZALERA
            print(f"Total payable: {total_money}$.")
            print(f"Fits you {round(money, 2)}$.")
            order.append(f"Extra Mozarela - {EXTRA_MOZALERA}$")
        case 3:
            print('You have selected extra chicken.'
                  f'\nExtra payable {EXTRA_CHICKEN}$.')
            money -= EXTRA_CHICKEN
            total_money += EXTRA_CHICKEN
            print(f"Total payable: {total_money}$.")
            print(f"Fits you {round(money, 2)}$.")
            order.append(f"Extra Chicken - {EXTRA_CHICKEN}$")
        case 4:
            print('Okay, no extra is added')
            break
        case _:
            print('Incorrect option, select one that is correct (1,2,3).')


menu_extra_ingredients(money, total_money)

if total_money <= money:
    print("\n--- You Order ---")

    print(f"Total your order: {total_money}$.")
    print(f"Your change: {money}$.\n")

    for i in order:
        print(f"-{i}.")

    print("\nEnojoy your meal!")
# Si el dinero no le llega, le indica que no le llega y no imprime el ticket.
else:
    print("You don't have the money for all that. Please start over.")

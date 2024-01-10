print('    ____     _                             _         \n'
      '   / __ \   (_) ____ ____  ___    _____   (_)  ____ _\n'
      '  / /_/ /  / / /_  //_  / / _ \  / ___/  / /  / __ `/\n'
      ' / ____/  / /   / /_ / /_/  __/ / /     / /  / /_/ / \n'
      '/_/      /_/   /___//___/\___/ /_/     /_/   \__,_/ ')

print('--------------------------------')

money = float(input('Please enter a money amount: '))

print('--------------------------------')

PIZZAS = ('Pizza Hawaiana', 'Pizza Siciliana', 'Pizza cuatro quesos')

PRICE_PIZZAS = (27.648, 37.400, 38.700)

EXTRA_INGREDIENTS = ('Extra queso', 'Extra mozarela', 'Extra pollo')

PRICE_EXTRA_INGREDIENTS = (3000, 2500, 3200)


def menu_order():
    cunter_menu = 1

    for p, v in zip(PIZZAS, PRICE_PIZZAS):
        print(f'{cunter_menu}) {p} - costo: {v}')
        cunter_menu += 1


menu_order()

print('--------------------------------')
selected_pizza_order = int(input('Por favor ingrese la opcion que desea: '))


def selected_pizza(option):
    if option == 1:
        print(f'El total hasta el momento es de: {PRICE_PIZZAS[0]}')
    elif option == 2:
        print(f'El total hasta el momento es de: {PRICE_PIZZAS[1]}')
    elif option == 3:
        print(f'El total hasta el momento es de: {PRICE_PIZZAS[2]}')
    else:
        print('Esa opcion no existe.')


selected_pizza(selected_pizza_order)
print('--------------------------------')

option_extra_ingredient = input('Do you want to add extra ingredient'
                                '(Yes or NO): ').lower()

if option_extra_ingredient == 'yes':
    contador = 1
    for p, v in zip(EXTRA_INGREDIENTS, PRICE_EXTRA_INGREDIENTS):
        print(f'{contador}) {p} - costo: {v}')
        contador += 1
elif option_extra_ingredient == 'no':
    print('-- Su pedido --\n'
          f'El total es de: {PRICE_PIZZAS[selected_pizza_order]}'
          f'Resta: {PRICE_PIZZAS[selected_pizza_order] - {money}}')
else:
    print('Esa opción no existe')

while True:
    choise = []
    chosen_option_extra_ingredient = input('\nPlease enter your choice: '
                                           ).lower()
    choise.append(chosen_option_extra_ingredient)
    option_exit = input('If you want to exit write "exit": ').lower()
    if option_exit == 'exit':
        break

print(choise)

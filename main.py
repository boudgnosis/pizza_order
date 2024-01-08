print('    ____     _                             _         \n'
      '   / __ \   (_) ____ ____  ___    _____   (_)  ____ _\n'
      '  / /_/ /  / / /_  //_  / / _ \  / ___/  / /  / __ `/\n'
      ' / ____/  / /   / /_ / /_/  __/ / /     / /  / /_/ / \n'
      '/_/      /_/   /___//___/\___/ /_/     /_/   \__,_/ ')

print('--------------------------------')

money = float(input('Please enter a money amount: '))

print('--------------------------------')

PIZZAS = ('Pizza Hawaiana', 'Pizza Siciliana', 'Pizza cuatro quesos')
print(type(PIZZAS))
PRICE_PIZZAS = (27.648, 37.400, 38.700)

EXTRA_INGREDIENTS = ('Extra queso', 'Extra mozarela', 'Extra pollo')

PRICE_EXTRA_INGREDIENTS = (3000, 2500, 3200)

contador = 1

for p, v in zip(PIZZAS, PRICE_PIZZAS):
    print(f'{contador}) {p} - costo: {v}')
    contador += 1

print('--------------------------------')

selected_pizza_order = int(input('Por favor ingrese la opcion que desea: '))

if selected_pizza_order == 1:
    print(f'El total hasta el momento es de: {PRICE_PIZZAS[0]}')
elif selected_pizza_order == 2:
    print(f'El total hasta el momento es de: {PRICE_PIZZAS[1]}')
elif selected_pizza_order == 3:
    print(f'El total hasta el momento es de: {PRICE_PIZZAS[2]}')
else:
    print('Esa opcion no existe.')

print('--------------------------------')

option_extra_ingredient = input('Do you want to add extra ingredient'
                                '(Yes or NO): ').lower()

if option_extra_ingredient == 'yes':
    contador = 1
    for p, v in zip(EXTRA_INGREDIENTS, PRICE_EXTRA_INGREDIENTS):
        print(f'{contador}) {p} - costo: {v}')
        contador += 1
    eleccion = input('What would you like to: ')
    if eleccion == '1':
        print(f'Su total es de: {PIZZAS}')
        pass
elif option_extra_ingredient == 'no':
    pass

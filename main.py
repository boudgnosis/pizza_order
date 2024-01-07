print('    ____     _                             _         \n'
      '   / __ \   (_) ____ ____  ___    _____   (_)  ____ _\n'
      '  / /_/ /  / / /_  //_  / / _ \  / ___/  / /  / __ `/\n'
      ' / ____/  / /   / /_ / /_/  __/ / /     / /  / /_/ / \n'
      '/_/      /_/   /___//___/\___/ /_/     /_/   \__,_/ ')

print('--------------------------------')

money = float(input('Please enter a money amount: '))

print('--------------------------------')

PIZZAS = {'Pizza Hawaiana': '27.648',
          'Pizza Siciliana': '37.400',
          'Pizza cuatro quesos': '38.700'
          }

EXTRA_INGREDIENTS = {
    'Extra queso': 3000,
    'Extra mozarela': 2500,
    'Extra pollo': 3200
}

contador = 1

for clave, valor in PIZZAS.items():
    print(f'{contador}) {clave} - costo: {valor}')
    contador += 1

print('--------------------------------')

selected_pizza_order = int(input('Por favor ingrese la opcion que desea: '))

if selected_pizza_order == 1:
    print('El valor de la Pizza hasta ahora es de:'
          f'{PIZZAS["Pizza Hawaiana"]}')

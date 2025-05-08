#Desarrollar un programa en Python que permita gestionar de manera eficiente el inventario de productos de una tienda, 
#aplicando funciones con parámetros, funciones lambda, y estructuras de datos como listas, tuplas y diccionarios.
#Eres parte del equipo de desarrollo de software de una tienda que desea mejorar la gestión de su inventario digital. 
# Te han asignado la tarea de crear un programa en Python que permita al equipo añadir, consultar, actualizar y eliminar 
# productos del inventario de manera eficiente, así como calcular el valor total del inventario. 
# Tu programa debe interactuar con el usuario para realizar las siguientes operaciones:

market = {}

# Añadir productos
def add_product(product, price, quantity):
    market[product] = {'Precio': price, 'Cantidad': quantity}
    print(f"Producto '{product}' añadido correctamente al inventario.")

# Consultar productos
def find_product(product):
    search = market.get(product, 'El producto no ha sido encontrado.')
    return search

# Actualizar precios
def update_price(product, price):
    if product in market:
        market[product]['Precio'] = price
        print(f"El precio del producto '{product}' ha sido actualizado a ${price:,.2f}.")
    else:
        print('El producto ingresado no ha sido encontrado.')

# Eliminar productos
def delete_product(product):
    if product in market:
        del market[product]
        print(f"Producto '{product}' eliminado del inventario.")
    else:
        print('El producto no existe en el inventario.')

# Calcular el valor total del inventario
def calculate_market():
    total = sum(market[prod]['Precio'] * market[prod]['Cantidad'] for prod in market)
    return f'\nEl total de todo el inventario de la tienda es ${total:,.2f}'

# Validar la entrada de un producto
def validate_product(product):
    while True:
        product = product.title()
        if product.isalnum():
            return product
        else:
            print('Error, el nombre del producto debe contener solo letras y números. Intenta nuevamente.')
            product = input('Ingresa el nombre del producto: ')

# Validar el precio ingresado
def validate_price(price):
    while True:
        try:
            price = float(price)
            if price > 0:
                return price
            else:
                print('Error, debes ingresar un número mayor a 0. Intenta nuevamente.')
                price = input('Ingresa el precio del producto: ')
        except ValueError:
            print('Error, debes ingresar un dato válido.')
            price = input('Ingresa el precio del producto: ')

# Validar la cantidad ingresada
def validate_quantity(quantity):
    while True:
        try:
            quantity = int(quantity)
            if quantity >= 0:
                return quantity
            else:
                print('Error, debes ingresar un número válido.')
                quantity = input('Ingresa la cantidad de unidades del producto: ')
        except ValueError:
            print('Error, debes ingresar un dato válido, intenta nuevamente.')
            quantity = input('Ingresa la cantidad de unidades del producto: ')

# Menú principal
def get_data():
    print('Bienvenido a la Tiendita\n')
    while True:
        option = input('\nIngresa un número para realizar alguna de las funciones\n'
                       '[1] Añadir producto\n'
                       '[2] Consultar productos disponibles\n'
                       '[3] Eliminar productos\n'
                       '[4] Reemplazar precios\n'
                       '[5] Calcular total del inventario\n'
                       '[6] Salir\n')

        match option:
            case '1':
                product = input('Ingresa el nombre de un producto: ')
                product = validate_product(product)
                price = input('Ingresa el precio del producto: ')
                price = validate_price(price)
                quantity = input('Ingresa la cantidad de unidades del producto: ')
                quantity = validate_quantity(quantity)
                add_product(product, price, quantity)
            case '2':
                product = input('Ingresa el nombre del producto a consultar: ')
                product = validate_product(product)
                result = find_product(product)
                print(result)
            case '3':
                product = input('Ingresa el nombre del producto a eliminar: ')
                product = validate_product(product)
                delete_product(product)
            case '4':
                product = input('Ingresa el nombre del producto a actualizar: ')
                product = validate_product(product)
                price = input('Ingresa el nuevo precio del producto: ')
                price = validate_price(price)
                update_price(product, price)
            case '5':
                total = calculate_market()
                print(total)
            case '6':
                break
            case _:
                print('Opción no válida. Intenta nuevamente.')

get_data()
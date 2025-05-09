"""
Eres un desarrollador junior en una empresa de software, y te han asignado la tarea de crear un
programa que calcule el costo total de una compra en una tienda. El programa debe interactuar con
el usuario a través de la consola, solicitando cuatro datos esenciales: el nombre del producto, el
precio unitario, la cantidad de productos adquiridos, y el porcentaje de descuento que se aplicará,
si es que existe alguno. Es fundamental que el programa maneje adecuadamente las entradas,
validando que tanto el precio como la cantidad sean números positivos, y que el descuento esté
dentro del rango aceptable de 0 a 100%.
Con estos datos, el programa debe calcular el costo total de la compra. Primero, debe determinar
el costo sin aplicar ningún descuento y, luego, si corresponde, aplicar el descuento especificado
para calcular el monto final. Además, este costo total debe ser mostrado junto con el nombre del
producto, de manera clara y formateada, asegurando que el resultado sea fácil de interpretar, por
ejemplo, presentando el valor con dos decimales.
Es importante que consideres la estructura y legibilidad de tu código, asegurándote de que esté
bien organizado y libre de errores. Por último, prueba el programa con distintos escenarios,
incluyendo casos extremos, para garantizar que funcione correctamente en todas las situaciones
posibles.
"""

#Una función que va a tomar todos los datos esenciales para ejecutar el programa.
def getData():
    
    #Para tomar el dato del nombre del producto, se crea un bucle el cual termina cuando el producto sea verdadero, 
    #el nombre del producto puede contener letras y número.
    while True:
        nameProduct = input("Ingrese el nombre del producto: ")
        if nameProduct.isalnum():
            break
        else:
            print("Error, datos no válidos, por favor ingrese solamente letras y números.\n")
    
    #Para tomar el precio del producto se utiliza otro bucle que termina cuando el precio arroje verdadero, debe ser tomado como un valor real.
    while True:
        try:
            priceProduct = input("Ingrese el precio unitario del producto: ")
            priceProduct = float(priceProduct)
            if (priceProduct > 0):
                break
            else:
                print("Error, el precio debe ser mayor a cero, intentelo nuevamente.\n")
        except ValueError:
            print("Error, ingresaste un dato no válido, vuelve a intentar por favor.\n")
    
    #Para tomar la cantidad de productos se ejecuta otro bucle que termina cuando la cantidad sea verdadera, 
    # la cantidad debe ser tomada como un valor entero.
    while True:
        try:
            cant = input("Ingrese la cantidad: ")
            cant = float(cant)
            if cant >= 0:
                break
            else:
                print("El número ingresa no es válido, por favor ingresa un número válido positivo.\n")
        except ValueError:
            print("Error, los datos ingresados no son válidos, por favor intente nuevamente.\n")
        
    #Para tomar el descuento se crea un bucle que termina cuando arroje verdadero, para este se específica que el descuento debe estar en el rango de 0 a 100.
    discount = 0
    while True:
        discount = input("Ingrese el porcentaje de descuento: ")
        if not discount:
            break
        try:
            discount = float(discount)
            if 0 <= discount <= 100:
                break
            else:
                print("El descuento ingresado no es válido, por favor ingresa un descuento entre 0 y 100.\n")
        except:
                print("Error, los datos ingresados no son válidos, por favor intente nuevamente\n")
    
    #Se retornan los datos para ser utilizados en otras funciones.
    return nameProduct, priceProduct, cant, discount

#Se crea una función para calcular el precio de los productos.
def calculatePrice(price, cant, discount ):

    subtotal = price * cant
    discountApply = subtotal*(discount/100)
    finalPrice = subtotal - discountApply
    
    #Se retornan los datos para ser utilizados en otras funciones.
    return  subtotal, discountApply, finalPrice

#Se crea una función la cual nos va a imprimir la lista del producto con la información.
def printPrice():
    product = []
    
    #Se llaman las variables de las funciones.
    name, price, cant, discount = getData()
    subtotal, discountApply, finalPrice = calculatePrice(price, cant, discount)
    
    #Añada nuevos elementos para ser tomados en la lista.
    product.append({
            "name": name,
            "price": price,
            "cant": cant,
            "discount": discount,
            "subtotal": subtotal,
            "discountApply": discountApply,
            "total": finalPrice
        })
    
    #Se imprime la lista y se le da un formato a los números para que se impriman con decimales y con puntos 
    # para así garantizar que la lista seŕa más legible para el usuario.
    print("\nTotal de compra\n")
    
    #Se utiliza un bucle para que llame las variables a la lista uno a uno. 
    for i, product in enumerate(product, 1):
        print(f"\nProducto: {product['name']}")
        print(f"  Precio unitario: ${product['price']:,.2f}")
        print(f"  Cantidad: {product['cant']}")
        print(f"  Subtotal: ${product['subtotal']:,.2f}")
        print(f"  Descuento aplicado: {product['discount']}% (-${product['discountApply']:,.2f})")
        print(f"\n  Total por producto: ${product['total']:,.2f}")
    
#Esta llama a la función e imprime los datos recolectados a lo largo del programa.
printPrice()
              
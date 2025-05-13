# 🎯 Inventario de una tienda 
🟣 En este documento, enseñaremos como ejecutar correctamente el programa **Inventory.py**, diseñado para llevar el inventario de una tienda que comenzará de cero. 

## 💻 Inicio 
El usuario debe iniciar el programa debe seguir la siguiente serie de pasos desde la terminal de su **Visual Studio Code**  
```python3 Inventory.py```

🟣 _Algo así se debería visualizar la terminal_

![image](https://github.com/user-attachments/assets/a0301ba0-3562-408a-87fc-40bb0b7e6619)


### ➡️ Bienvenida
Al ejecutar el código, el usuario observará un mensaje de bienvenida al programa.
Se le desplegará el menú, en el cuál deberá ingresar un número para realizar alguna de las funciones descritas.

🟣 _Mensaje de bienvenida al usuario_

![image](https://github.com/user-attachments/assets/a70974f5-2ed4-4565-bda8-aa4d1ec28970)


### ➡️ Validaciones

El ingreso de productos tiene 3 validaciones:

🟣 **Nombre**: El nombre no puede contener carácteres especiales, solo puede contener letras y números. Se pueden escribir espacios ya que el programa se encarga de eliminarlos automáticamente.
_Ejemplos de como escribir un nombre_
```
✅ CocaCola300ml
✅ coca cola 300 ml
✅ COCA COLA 300 ML

❌ CocaCola*300
'ERORR'
```

🟣 **Precio**: Solamente se pueden ingresar números mayores a cero, pueden ser enteros o reales.

_Ejemplos de como escribir un precio_
```
✅ 300.2
✅ 34581

❌ 31,5465.5
❌ -524
'ERORR'
```

🟣 **Cantidad**: Solamente se pueden ingresar números mayores a cero y únicamente pueden ser números enteros.

_Ejemplos de como escribir una cantidad_
```
✅ 34

❌ 31,7
❌ -524
'ERORR'
```

## 🎯 Añadir productos [1]
El programa por defecto añadirá productos mientras la cantidad de productos sea menor a 5, pero, ya cuandop hayan 5 productos se pueden añadir más desde el menú sin nigún tipo de problema

🟣 Al añadir nuevos productos, se validará que cada uno de los datos ingresados sean válidos.
🟣 Si un dato es inválidado se volverá a solicitar al usuario que ingrese el dato.

_Así se debería visualizar la terminal mientras los datos sean correctos_

![image](https://github.com/user-attachments/assets/a8e335ca-58d7-44b5-aa50-a59874e6193d)

_Así se debería visualizar la terminal mientras los datos sean incorrectos_

![image](https://github.com/user-attachments/assets/389f67a4-1ee2-4d75-b058-37c74c4aa008)


## 🎯 Buscar productos [2]

El usuario debe ingresar un nombre del producto que quiera buscar en su inventario.

🟣 Si el producto ingresado se encuentra en el inventario se mostrará al usuario el precio y la cantidad de productos disponibles en el momento.

![image](https://github.com/user-attachments/assets/f46042fa-ce79-4b28-a644-aa2709afc69a)

🟣 Si el producto ingresado no se encuentra en el inventario aparecerá un mensaje indicando que no se encontró el producto.

![image](https://github.com/user-attachments/assets/11b0c7a2-44f5-426d-975b-7fe2807a6ebc)


## 🎯 Eliminar productos [3]
El usuario debe ingresar el nombre del producto el cual quiere eliminar.

🟣 Si ya no existen unidades disponibles del producto (0), entonces el producto se eliminará del inventario.

![image](https://github.com/user-attachments/assets/d251526f-1c02-4046-941d-779fac8f1677)


🟣 Si existen aún unidades del producto el programa arrojará un mensaje diciendo que aún existen unidades disponibles, por lo cual no eliminará el producto.

![image](https://github.com/user-attachments/assets/5938e7e6-6b26-4bc5-b7b3-e8613a616ca5)


## 🎯 Actualizar productos [4]
El usuario tiene la opción de actualizar el precio y la cantidad de productos que quiere tener disponibles en el inventario.


🟣 Si el producto existe, se actualizará y se le mostrará un mensaje al usuario con el precio y la cantidad de productos.



![image](https://github.com/user-attachments/assets/0b2ee35a-adc5-4a10-927d-d2c9a8e7c75e)


🟣 Si el producto no existe, se le indicará al usuario que el producto no fue encontrado.

![image](https://github.com/user-attachments/assets/57250e7b-dc2f-489a-9001-66ed013c43e0)


## 🎯 Calcular total de inventario [5]
En esta opción el programa calculará automáticamente todos los productos que el usuario tenga disponibles en el inventario.

🟣 Se mostrará un mensaje indicando cual es el total neto del inventario.

![image](https://github.com/user-attachments/assets/5fe33a0a-7684-49ab-a682-712bb63bff6f)

## 🎯 Salir [6]
Con esta opción el usuario cerrará el programa y se mostrará un mensaje en la terminal indicando esto.

![image](https://github.com/user-attachments/assets/4d86ea57-a758-47d7-8141-2996a2d6dd85)








number= input("Ingresa un número entero: ")

if number.isdigit() or (number.startswith("-")) and number[1:].isdigit():
    n = int(number)
    if n % 15 == 0:
                print("FizzBuzz")
    elif n % 3 == 0:
                print("Fizz")
    elif n % 5 == 0:
                print("Buzz")
    else:
                print("El número no es múltiplo de 3, 5 y 15.")
else:
     print("No se aceptan decimales ni caracteres inválidos.")
def check_number():
    while True:
        num = input("Ingresa un número: ")
        try:
            num = float(num)
            return num
        except:
            print("Ingresaste un dato no válido.")

number = check_number()

if number < 0:
    print("El número es negativo.")
elif number == 0:
    print("El numero es cero.")
else:
    print("El número es positivo.")
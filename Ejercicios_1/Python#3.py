def check_number():
    while True:
        num = input("Ingresa un número entero: ")
        try:
            num = int(num)
            return num
        except:
            print("El número ingresado no es válido.")

number = check_number()
if number % 2 == 0:
    print("Es par.")
else:
    print("Es impar.")
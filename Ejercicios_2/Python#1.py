def check_number():
    while True:
        num = input("Ingresa un número: ")

        try:
            num = float(num)
            return num
        except:
            print("Ingresaste un dato no válido.")

n1 = check_number()
n2 = check_number()
sum = n1 + n2
print("La suma de " + str(n1) + " y " + str(n2) + " es: " + str(sum))
                
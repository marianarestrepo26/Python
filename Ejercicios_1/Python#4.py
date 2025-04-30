while True:
    
    enterNum = input("Ingresa un número entero: ")

    if not enterNum.isdigit():
        print("Deber ingresar un número.")
        continue
    
    number = int(enterNum)
    if number < 0:
        print("El número ingresado debe ser positivo.")

    def is_prime(num):
        if (num < 2):
            return False
        
        for i in range(2, num-1):
            if (num % i == 0):
                return False
        return True
    
    if (is_prime(number)):
        print("El número es primo")
    else:
        print("El número no es primo")
    
    break
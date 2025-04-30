import random

numero_secreto = random.randint(1, 10)

while True:
    intento = input("Adivina el número entre 1 y 10: ")

    if intento.isdigit():
        intento = int(intento)
        
        if intento < 1 or intento > 10:
            print("El número debe estar entre 1 y 10")
        elif intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print("Adivinaste el número.")
            break
    else:
        print("Ingresa un número válido.")

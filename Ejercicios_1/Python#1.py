def check_age(nombre):
    while True:
        age = input("Ingresa tu edad: ")
        if age.isdigit():
            return int(age)
        elif age.startswith("-"):
            print("El número ingresado es negativo, por favor ingresa una edad válida")
        else:
            print("El dato ingresado no es válido.")

p1 = input("Ingresa tu nombre: ")
age1 = check_age(p1)
p2 = input("Ingresa tu nombre: ")
age2 = check_age(p2)


if age1 > age2:
    print(p1 + " es mayor.")
elif age1 < age2: 
    print(p2 + " es mayor.")
else: 
    print("Ambos tienen la misma edad.")


if age1 >= 18 and age2 < 18:
    print(p1 + " es mayor de edad")
elif age1 < 18 and age2 >= 18:
    print(p2 + " es mayor de edad")
elif age1 < 18 and age2 < 18:
    print("Los dos son menores de edad.")
else:
    print("Los dos son mayores de edad.")
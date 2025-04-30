def check_age():
    while True:
        age = input("Ingresa tu edad: ")
        if age.isdigit():
            return int(age)
        elif age.startswith("-"):
            print("Por favor ingresa una edad válida.")
        else:
            print("El dato ingresado no es válido.")
            
age5 = check_age() + 5
print(f"En 5 años tendrás {age5} años.")
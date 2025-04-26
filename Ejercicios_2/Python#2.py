def pedir_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.isalpha():
            print(f"¡Hola, {nombre}!")
            break
        else:
            print("El nombre solo debe contener letras.")

pedir_nombre()
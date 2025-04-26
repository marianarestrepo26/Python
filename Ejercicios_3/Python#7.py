def menu():
    print("\nMENÚ")
    print("1=Saludar")
    print("2=Mostrar fecha y hora")
    print("3=Salir")

while True:
    menu()
    opcion = input("Selecciona una opción (1,2,3): ")
    
    match opcion:
        case "1":
            print("Hola, ¿Cómo estás?")
        case "2":
            import datetime
            ahora = datetime.datetime.now()
            print(f"Fecha y hora actual: {ahora}")
        case "3":
            print("Hasta luego.")
            break
        case _:
            print("Opción no válida.")

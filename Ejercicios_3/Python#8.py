def clasificar_nota(nota):
    match nota:
        case 5:
            return "Excelente"
        case 4:
            return "Muy bien"
        case 3:
            return "Bien"
        case 2:
            return "Suficiente"
        case 1:
            return "Muy mal"
        case _:
            return "Debe ser un número entre 1 y 5."

while True:
    try:
        nota = int(input("Ingresa una nota entre 1 y 5: "))
        if 1 <= nota <= 5:
            print(clasificar_nota(nota))
            break
        else:
            print("LLa nota debe estar entre 1 y 5.")
    except ValueError:
        print("Ingresa un número válido.")

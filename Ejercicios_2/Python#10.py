note_input = input("Ingrese su nota: ")

def validar_nota(nota):
    try:
        nota = int(nota)
        if 0 <= nota <= 100:
            return nota
        print("La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Debe ingresar una nota válida.")
    return None

nota_valida = validar_nota(note_input)

if nota_valida is not None:
    print("Aprobado" if nota_valida >= 60 else "Reprobado")

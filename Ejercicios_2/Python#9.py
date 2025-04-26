def es_numero(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

while True:
    print("\nOperaciones aritméticas")
    print("+  -  *  /")
    print("X para salir")

    op = input("Opción: ")
    if op == 'X':
        break

    n1 = input("Ingrese un número: ")
    n2 = input("Ingrese otro número: ")

    if not (es_numero(n1) and es_numero(n2)):
        print("Por favor ingrese números válidos.")
        continue

    n1, n2 = float(n1), float(n2)

    if op == '+':
        print(f"Resultado: {n1 + n2}")
    elif op == '-':
        print(f"Resultado: {n1 - n2}")
    elif op == '*':
        print(f"Resultado: {n1 * n2}")
    elif op == '/':
        if n2 == 0:
            print("No se puede dividir por cero.")
        else:
            print(f"Resultado: {n1 / n2}")
    else:
        print("Opción no válida.")

def tipo_dia(dia):
    match dia.lower():
        case "lunes" | "martes" | "miércoles" | "jueves":
            return "Es un día de la semana."
        case "viernes":
            return "Es viernes."
        case "sabado" | "domingo":
            return "Es fin de semana."
        case _:
            return "Por favor ingresa un día de la semana."

while True:
    dia = input("Ingresa un día de la semana: ")
    
    if dia.isalpha(): 
        print(tipo_dia(dia))
        break
    else:
        print("Por favor ingresa un día de la semana válido.")

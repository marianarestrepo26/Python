def check_age():
    while True:
        note = input("Ingresa una nota: ")
        try:
            note = float(note)
            if 0 < note < 5:
                return note
            else:
                print("La nota debe estar entre 0 y 5.")
        except:
            print("Ingresaste un dato no válido.")
        
name=input("Ingrese su nombre: ")

n1 = check_age()
n2 = check_age()
n3 = check_age()
n4 = check_age()
n5 = check_age()

nProm= (n1 + n2 + n3 + n4 + n5)/5

print(name)
print(nProm)

if nProm >= 3.0:
    print("Ganaste.")
else: 
    print("Perdiste la materia.")
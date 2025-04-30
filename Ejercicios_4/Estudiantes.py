#Crea un diccionario de estudiantes donde las claves sean los nombres y los valores sus notas finales.
#Después imprime los nombres de los estudiantes que aprobaron (nota mayor o igual a 6).

students = {
    "Mariana": 10.0,
    "Ramiro": 3.0,
    "Julian": 7.0,
    "Jorge": 5.5,
    "Alejandra": 7.0
}

print("Estudiantes que ganaron el año:")
for name, note in students.items():
    if note >= 6:
        print(name)

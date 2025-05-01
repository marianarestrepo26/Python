#Desarrolla un programa en Python que gestione una serie de calificaciones y estadísticas de manera interactiva.


#Determinar el estado de aprobación
def approve():
    while True:
        name = input(f'Ingresa el nombre del estudiante a evaluar: ')
        if (name.isalpha() or name.isspace()):
            break
        else:
            print('Error, por favor ingresa un nombre válido.')

    #Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
    while True:
        get_note = input(f'Ingresa la calificación de {name} entre 0 y 100: ')
        try:
            get_note = float(get_note)
            if 0 <= get_note <= 100:
                #Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
                if 60 <= get_note:
                    print(f'{name} ha aprobado.')
                else:
                    print(f'{name} ha reprobado.')
            else:
                print('La nota debe estar entre 0 y 100.')
        except:
            print('Ingresaste un dato no válido.')

#Calcular el promedio del estudiante
def calculate_mean():
    l = 0
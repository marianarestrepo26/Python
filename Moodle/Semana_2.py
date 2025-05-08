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
                if 60 <= get_note:
                    print(f'{name} ha aprobado.')
                    return f'{name}: Aprobado con {get_note}'
                else:
                    print(f'{name} ha reprobado.')
                    return f'{name}: Reprobado con {get_note}'
            else:
                print('La nota debe estar entre 0 y 100.')
        except ValueError:
            print('Ingresaste un dato no válido.')

#Calcular el promedio del estudiante
def calculate_mean():
#Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    while True:
        try:
            get_note = input('Ingresa las calificaciones separadas por comas: ')
            note = [float(i.strip()) for i in get_note.split(',')]
            if all(0 <= i <= 100 for i in note):
    #Calcular y mostrar el promedio de las calificaciones en la lista
                prom = sum(note) / len(note)
                print(f'El promedio de las calificaciones es: {prom}')
                return note, f'Promedio: {prom}'
            else:
                print('Todas las calificaciones deben estar entre 0 y 100.')
        except ValueError:
            print('Error, debes de ingresar solo números separados por comas.')

#Contar calificaciones mayores
def mayor_note(note):
    if not note:
        print('No hay calificaciones válidas para evaluar.')
        return 'Error: No se pudo contar calificaciones mayores.'
    #Preguntar al usuario por un valor específico
    while True:
        try:
            mayor = float(input('Ingresa un valor para contar calificaciones mayores: '))
    #Contar cuántas calificaciones en la lista son mayores que este valor
            counter = sum(1 for grade in note if grade > mayor)
            print(f'Cantidad de calificaciones mayores a {mayor}: {counter}')
            return f'Calificaciones mayores a {mayor}: {counter}'
        except ValueError:
            print('Error: Asegúrate de ingresar solo números válidos.')

#Verificar y contar calificaciones específicas
def check_note(note):
    while True:
#Preguntar al usuario por una calificación específica. 
        try:
            search = float(input('Ingresa la nota que vas a buscar: '))
        #Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa.   
            count = 0
            for i in note:
                if i == search:
                    count += 1  
            return(f'La calificación {search} aparece en la lista : {count} veces.')  
        except ValueError:
            print('Error, debes de ingresar un número válido.')

#Mostrar todo el programa en la terminal.
def print_note():
    results = []  # Se crea una lista para almacenar los resultados de cada estudiante
    while True:
        print('\nEstado de aprobación')
        results.append(approve())

        print('\nPromedio de calificaciones')
        note, mean_result = calculate_mean()
        results.append(mean_result)

        print('\nCalificaciones mayores')
        results.append(mayor_note(note))

        print('\nContar calificaciones')
        results.append(check_note(note))

        try:
            another_student = input('\n¿Quieres evaluar a otro estudiante? (SI/NO): ')
            if another_student.upper() == 'NO':
                print('\nResumen de todas las operaciones realizadas')
                for result in results:
                    print(result)
                break
        except Exception:
            print('Error, debes de ingresar SI o NO.')

print_note()


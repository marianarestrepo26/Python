#Crea una pequeña agenda que permita:
#Agregar un nuevo contacto (nombre y número de teléfono).
#Buscar un contacto por su nombre.
#Mostrar todos los contactos.
#Eliminar un contacto.
#Requisitos:
#Usar un diccionario donde el nombre sea la clave y el número sea el valor.
#Crear un pequeño menú en consola para elegir las acciones.

contacts = {"MADRE" : "3157987457",
             "HERMANO" : "3481524879",
             "MARIANA" : "3548756641",
             "CASA" : "6048751542"}

def newContact (contacts):
    name = input("Nombre del contacto: ")
    name = name.upper()
    phone = input("Télefono del contacto: ")

    contacts[name] = phone
    print("\nNuevo contacto agregado")
                    

def searchContact(contacts):
    contact = input("Ingresa el nombre del contacto que quieres buscar: ")
    contact = contact.upper()
    if contact in contacts:
        phone = contacts[contact]
        print(f"El número de {contact} es: {phone}")
    else:
        print("Contacto ingresado no está registrado.\n")


def deleteContact(contacts):
    contact = input("Ingresa el nombre del contacto que quieres eliminar: ")
    contact = contact.upper()
    if contact in contacts:
        del contacts[contact]
        print(contacts)



def showContacts():
    for contact, phone in contacts.items():
        print(f'{contact} : {phone}')

def menu():
    cont = input("\nBienvenido a tu lista de contactos \n"
    'Ingresa una letra para realizar alguna de las siguientes funciones\n'
    "\n[A] Agregar un contacto  \n" 
    "[B] Buscar un contacto por nombre \n" 
    "[E] Eliminar un contacto \n"
    "[M] Mostrar todos los contactos \n" 
    "[S] Salir \n")
    cont = cont.upper()
    
    match cont:
        case "A":
            newContact(contacts)
            menu() 
        case "B":
            searchContact(contacts)
            menu()
        case "E":
            deleteContact(contacts)
            menu()
        case "M":
            showContacts()
            menu()
        case "S":
            exit()

menu()
while True:
    palabra = input("Ingresa una palabra: ")
    
    if palabra.isalpha(): 
        for letra in palabra:
            print(letra.upper())
        break  
    else:
        print("Solo puedes ingresar letras.")

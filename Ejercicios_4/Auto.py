#Crea un diccionario llamado auto que contenga: Marca, Modelo, Año
#Cambia el modelo del auto a otro diferente.
#Agrega una nueva clave color al diccionario.
#Elimina la clave año.
#Imprime todas las claves del diccionario usando un bucle for.
#Imprime todos los valores del diccionario usando un bucle for.

auto ={
    "Brand" : "Toyota",
    "Model" : "Txl",
    "Age" : "2022"
}
print(auto)

auto['Model'] = 'A 180'

auto['Color'] = 'White'

del auto['Age']

for brand, info in auto.items():
    print(f'{brand} : {info}')
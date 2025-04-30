#Crea un diccionario paises donde las claves sean nombres de países y los valores sus capitales.
#Escribe un programa que pregunte al usuario un país y devuelva su capital (si existe).
#Invierte el diccionario paises, es decir, que las capitales sean las claves y los países los valores.

countries = {
    'Colombia': 'Bogotá',
    'Cuba': 'La Habama',
    'Uruguay': 'Montevideo',
    'Noruega': 'Oslo',
    'Italia' : 'Roma'
}

country = input('Escribe un país: ')
if country in countries:
    print(f'La capital de {country} es: {countries[country]}')
else:
    print('País no encontrado')

invertCountry = {}

for country in countries:
    capital = countries[country]
    invertCountry[capital] = country
    
print(invertCountry)
#Inventory for a store

#Dictionary void
store = {}

#VALIDATION FUNCTIONS

#Validate name of products
def val_product(product):
    #Repeat the cycle until the product name is valid
    while product:
        #Validate if the product is number or letter and delete space.
        product = product.title().replace(" ", "")
        if product.isalnum():
            return product
        else:
            print('Error, you must inssert a valid name. Try again.')
            #Request the user to re-enter the name
            product = input('Enter product name: ')

def val_price(price):
    #Repeat the cycle until the product price is valid
    while price:
        try:
            #Validate if the price is a real number
            price = float(price)
            #Validate if the price is major than 0.
            if price > 0:
                return price
            else:
                print('Error, the price must be a positive number. Try again.')
                price = input('Enter the product price: ')
        except:
            print('Error, you must inssert a valid price. Try again.')
            price = input('Enter the product price: ')

def val_quantity(quantity):
    #Repeat the cycle until the product quantity is valid
    while quantity:
        #Validate if the quantity is a whole number.
        try:
            quantity = int(quantity)
            #Validate if the price is major or equal than 0.
            if quantity >= 0:
                return quantity
            else:
                print('Error, the quantity must be a positive number. Try again.')
                quantity = input('Enter the quantity of products: ')
        except:
            print('Error, you must inssert a valid quantity. Try again.')
            quantity = input('Enter the quantity of products: ')

#PROCESS

#Add products in the inventory
def add_prod():
    product = input('\nEnter the product name: ')
    product = val_product(product)
    if product in store:
        print('Error, the product is exist.')
        product = input('\nEnter the product name: ')
    price = input('Enter the product price: ')
    price = val_price(price)
    quantity = input('Enter the products quantity: ')
    quantity = val_quantity(quantity)
    
    store[product] = {'Price' : price, 'Quantity' : quantity}
    print(f"Product '{product}' added correctly.\n")
    

#Search products in the inventory
def search_prod(product):
    #Search the product in the dictionary
    find = store.get(product, 'Product has no been found.\n')
    return find

#Update prices of the product 
def updatePrice_prod(product, price, quantity):
    #Validate if the product that we find is in store.
    if product in store:
        store[product]['Price'] = price
        store[product]['Quantity'] = quantity
        print(f"Price of the product '{product}' has been updated, new price is ${price:,.2f} and has {quantity} units.\n")
    else:
        print(f"Product '{product}' has no been found.")

#Remove products in the inventory
def remove_prod(product):
    #Validate if product is in the inventory.
    if product in store:
        if store[product]['Quantity'] == 0: 
            del store[product]
            print(f"Product '{product}' has been remove to the inventory.\n")
        else:
            print(f'Error, {product} still has products available.\n')
    else:
        print(f"Error, the product '{product}' has no been found.\n")

#Calculate total in the inventory
def calculate_inventory():
    #Sum all prices multiplied by the quantity.
    total = sum(store[prod]['Price'] * store[prod]['Quantity'] for prod in store)
    return f"\nThe total for the everything in the inventory is: ${total:,.2f}"


#Main menu for do the functions and get data
def menu_inventory():
    print("\nWELCOME TO MARIANA'S STORE\n")

    while True:
        option = input('\nEnter a number to do a function: \n'
                       '[1] Add a new product.\n'
                       '[2] Find available products.\n'
                       '[3] Remove products.\n'
                       '[4] Update prices.\n'
                       '[5] Calculate total inventory.\n'
                       '[6] Exit.\n'
                       'Option: ')
#Depending on the number chosen by the user, one of the functions will be make.
        match option:
            case '1':
                #Validate if the inventory has 5 or more products
                while len(store) < 4:
                    add_prod()
                else:
                    add_prod()
            case '2':
                product = input('Enter the product name that you want search: ')
                product = val_product(product)
                result = search_prod(product)
                print(result)
            case '3':
                product = input('Enter the product name that you want remove: ')
                product = val_product(product)
                remove_prod(product)
            case '4':
                product = input('Enter the product name that you want update: ')
                product = val_product(product)
                price = input('Enter the new product price: ')
                price = val_price(price)
                quantity = input('Enter the new product quantity: ')
                quantity = val_quantity(quantity)
                updatePrice_prod(product, price, quantity)
            case '5':
                total = calculate_inventory()
                print(total)
            case '6':
                print('Leaving the program...')
                break
            case _:
                print('Error, option no valid. Try again.')

#Calls the function to return every the function has.
menu_inventory()


while True:
    try:
        total = 0

        for num in range(1, 11):
            total += num

        print(f"La suma de los primeros 10 números es: {total}")
        break
    except ValueError:
        print("S10olo puedes ingresar números.")

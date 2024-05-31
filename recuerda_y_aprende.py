import random

print("Recuerda la combinación!!")

while True:
    print("""
    ¿Estás listo? (escoge una opción)
    
    1) Empezar
    2) Salir
    """)
    opcion = int(input("Elige una opción: "))     

    if opcion == 2:
        break
    elif opcion == 1:
        print("¡Empecemos!")
        numeros_repetidos = [random.randint(0, 9) for _ in range(16)]
        print(numeros_repetidos)
        recuerda = input("Introduce los números agregados (sin espacios): ")

        # Verificación
        if recuerda.isdigit() and len(recuerda) == 16:
            recuerda_lista = [int(digito) for digito in recuerda]
            if recuerda_lista == numeros_repetidos:
                print("¡Felicidades!")
            else:
                print("Vuelve a intentarlo")
        else:
            print("Ingresa 16 dígitos numéricos sin espacios.")
    else:
        print("Opción incorrecta")

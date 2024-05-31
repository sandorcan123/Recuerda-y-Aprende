import random
import time

record = 0  # Variable para almacenar el récord

print("Recuerda la combinación!!")

while True:
    print("""
    ¿Estás listo? (escoge una opción)
    
    1) Empezar
    2) Salir
    3) Mostrar récord
    """)
    opcion = int(input("Elige una opción: "))     

    if opcion == 2:
        break
    elif opcion == 1:
        print("¡Empecemos!")
        numeros_repetidos = [random.randint(0, 9) for _ in range(16)]
        print(numeros_repetidos)

        inicio_tiempo = time.time()
        recuerda = input("Introduce los números agregados (sin espacios): ")
        tiempo_transcurrido = time.time() - inicio_tiempo
        puntos = int(100 / tiempo_transcurrido)  # Calcula los puntos según el tiempo

        if recuerda.isdigit() and len(recuerda) == 16:
            recuerda_lista = [int(digito) for digito in recuerda]
            if recuerda_lista == numeros_repetidos:
                print(f"¡Felicidades! Obtuviste {puntos} puntos.")
                if puntos > record:
                    record = puntos
            else:
                print("Vuelve a intentarlo")
        else:
            print("Ingresa 16 dígitos numéricos sin espacios.")
    elif opcion == 3:
        print(f"Mejor récord: {record} puntos")
    else:
        print("Opción incorrecta")

import random
import time

record_tiempo = float("inf")  # Inicializamos el récord con infinito (para que cualquier tiempo sea menor)

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

        if recuerda.isdigit() and len(recuerda) == 16:
            recuerda_lista = [int(digito) for digito in recuerda]
            if recuerda_lista == numeros_repetidos:
                print(f"¡Felicidades! Completaste la combinación en {tiempo_transcurrido:.2f} segundos.")
                if tiempo_transcurrido < record_tiempo:
                    record_tiempo = tiempo_transcurrido
            else:
                print("Vuelve a intentarlo")
        else:
            print("Ingresa 16 dígitos numéricos sin espacios.")
    elif opcion == 3:
        if record_tiempo == float("inf"):
            print("Aún no hay récord establecido.")
        else:
            print(f"Mejor récord: {record_tiempo:.2f} segundos")
    else:
        print("Opción incorrecta")

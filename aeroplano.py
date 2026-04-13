# 1. Declaración de variables usando la nomenclatura snake_case
bateria_dron = 100
altitud_actual = 0

print("--- INICIANDO SIMULADOR DE DRON ---")

# 2. Bucle condicionado (sin usar 'while True')
while bateria_dron > 0:
    # 3. Pedimos la orden y la hacemos a prueba de fallos con .lower()
    maniobra = input("¿Qué maniobra deseas realizar? (Subir / Planear): ").title()
    
    # 4. Evaluamos la maniobra y aplicamos operadores de asignación compuesta (-=)
    if maniobra == "Subir":
        bateria_dron -= 15
        altitud_actual += 10  # Aumentamos altitud como extra lógico
        print("Elevando el dron...")
    elif maniobra == "Planear":
        bateria_dron -= 5
        print("Planeando y analizando el terreno...")
    else:
        print("Comando no reconocido. El dron se mantiene en posición.")
        
    # Evitamos que la batería muestre números negativos si baja de 0 de golpe
    if bateria_dron < 0:
        bateria_dron = 0

    # 5. Imprimimos el estado con una cadena formateada (f-string)
    print(f"Te queda {bateria_dron}% de batería. Altitud actual: {altitud_actual}m.\n")

# 6. Advertencia final fuera del bucle
print("¡Advertencia! Batería agotada. El dron aterriza automáticamente.")
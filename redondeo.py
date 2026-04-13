# 1. Declaración de constantes (Siempre en mayúsculas)
PRECIO_VIP = 75

# 2. Solicitamos los datos al usuario
# Convertimos la edad a un número entero con int() para operar lógicamente
edad = int(input("Por favor, introduce tu edad: "))

# Hacemos el input a prueba de fallos convirtiendo todo a mayúsculas con .upper()
codigo = input("Introduce tu código de descuento (si no tienes, pulsa Enter): ").upper()

# 3. Estructura de control if / elif / else desglosada
if edad < 18:
    # Denegamos el acceso a menores
    precio_final = 0
    print("Acceso denegado: Debes ser mayor de edad para acceder a la zona VIP.")
    
elif codigo == "VERANOVIP":
    # Descuento de 20 euros
    precio_final = PRECIO_VIP - 20
    print("Descuento VERANOVIP aplicado correctamente.")
    
elif codigo == "ESTUDIANTE":
    # Descuento de 10 euros
    precio_final = PRECIO_VIP - 10
    print("Descuento ESTUDIANTE aplicado correctamente.")
    
else:
    # Caso por defecto: mayor de edad pero sin código válido
    precio_final = PRECIO_VIP
    print("No se ha introducido ningún código válido.")

# 4. Mensaje final mostrando el resultado si tiene acceso
if precio_final > 0:
    # Imprimimos usando f-strings para modernizar la sintaxis
    print(f"El importe a pagar por tu entrada VIP es de {precio_final} euros.")
 
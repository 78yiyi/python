
"""
SISTEMA DE GESTIÓN "PYTHON ACADEMY"
Autor: [Tu Nombre]
Descripción: Ejercicio integrador para cubrir los RAs del módulo.
"""
# RA1 i) Se han introducido comentarios en el código.

import sqlite3  # RA2 e) Incorporación y utilización de librerías.
import os       # RA5 c) Posibilidades de entrada/salida y librerías asociadas.

# --- FASE 4: PROGRAMACIÓN ORIENTADA A OBJETOS (RA4) ---

class Persona:
    # RA4 a) Definición de clases.
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    # RA4 b) Uso del concepto de herencia.
    def __init__(self, nombre):
        super().__init__(nombre)
        # RA4 c) Condiciones de acceso (atributo privado __calificaciones).
        self.__calificaciones = []

    def agregar_nota(self, nota):
        # Método público para modificar atributo privado.
        self.__calificaciones.append(nota)
    
    def obtener_notas(self):
        return self.__calificaciones

# --- FASE 2: LÓGICA Y FUNCIONES (RA2) ---

def calcular_promedio(lista_notas):
    # RA2 c, d) Uso de funciones y parámetros.
    if not lista_notas:
        return 0
    # RA1 g) Uso de operadores algebraicos (+ y /).
    suma_total = sum(lista_notas)
    return suma_total / len(lista_notas)

# --- FASE 6: BASES DE DATOS (RA6) ---

def inicializar_bd():
    # RA6 a, b) Acceso y conexión a BBDD relacionales.
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()
    # RA6 c, f) Código para almacenar y ejecutar consultas SQL.
    cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos 
                      (id INTEGER PRIMARY KEY, nombre TEXT, promedio REAL)''')
    conn.commit()
    return conn

# --- FASE 1 Y 3: FLUJO PRINCIPAL, SELECCIÓN Y REPETICIÓN (RA1, RA3, RA5) ---

def main():
    # RA5 a) Uso de la consola para salida.
    print("=== BIENVENIDO A PYTHON ACADEMY ===")
    
    # RA1 f) Uso de literales y constantes (convención MAYÚSCULAS).
    NOTA_MINIMA = 5.0
    
    # RA5 a) Uso de la consola para entrada.
    admin_nombre = input("Introduce tu nombre de administrador: ")
    # RA5 b) Formatos en la visualización (f-strings).
    print(f"Sesión iniciada: {admin_nombre}")

    conn = inicializar_bd()
    cursor = conn.cursor()

    # RA3 b) Estructuras de repetición (bucle para varios alumnos).
    while True:
        nombre_alumno = input("\nNombre del alumno (o 'fin' para salir): ")
        if nombre_alumno.lower() == 'fin':
            break

        nuevo_estudiante = Estudiante(nombre_alumno)

        for i in range(1, 4):
            # RA3 d, f) Control de excepciones y depuración.
            try:
                # RA1 h) Conversión de tipo (str a float).
                nota = float(input(f"Introduce nota {i}: "))
                nuevo_estudiante.agregar_nota(nota)
            except ValueError:
                print("Error: ¡Debes introducir un número!")
                continue

        promedio = calcular_promedio(nuevo_estudiante.obtener_notas())

        # RA3 a) Estructuras de selección (if-elif-else).
        if promedio >= 9:
            estado = "Sobresaliente"
        elif promedio >= 7:
            estado = "Notable"
        elif promedio >= NOTA_MINIMA:
            estado = "Aprobado"
        else:
            estado = "Suspenso"

        print(f"Resultado de {nuevo_estudiante.nombre}: {promedio:.2f} ({estado})")

        # RA6 c) Código para almacenar información en la BD.
        cursor.execute("INSERT INTO alumnos (nombre, promedio) VALUES (?, ?)", 
                       (nuevo_estudiante.nombre, promedio))
        conn.commit()

        # --- FASE 5: FICHEROS (RA5) ---
        # RA5 d, e) Uso de ficheros para almacenar información.
        with open("notas.txt", "a") as archivo:
            archivo.write(f"Alumno: {nuevo_estudiante.nombre} - Promedio: {promedio:.2f}\n")

    # RA6 d) Recuperar y mostrar información de la BD.
    print("\n--- REPORTE FINAL DESDE BASE DE DATOS ---")
    cursor.execute("SELECT * FROM alumnos")
    for fila in cursor.fetchall():
        print(f"ID: {fila} | Estudiante: {fila} | Media: {fila}")

    conn.close()
    print("\nPrograma finalizado y datos guardados.")

if __name__ == "__main__":
    main()



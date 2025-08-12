import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("WolfLone")
ventana.geometry("800x600")

# Crear el Notebook (pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand=True)

# Pestaña 1: HOJA DE PERSONAJE
frame_personaje = ttk.Frame(notebook)
notebook.add(frame_personaje, text="HOJA DE PERSONAJE")

# Ejemplo de contenido para la pestaña 1
label1 = tk.Label(frame_personaje, text="Aquí va la hoja de personaje", font=("Arial", 16))
label1.pack(pady=20)

# Pestaña 2: REGISTRO DE COMBATE
frame_combate = ttk.Frame(notebook)
notebook.add(frame_combate, text="REGISTRO DE COMBATE")

# Ejemplo de contenido para la pestaña 2
label2 = tk.Label(frame_combate, text="Aquí va el registro de combate", font=("Arial", 16))
label2.pack(pady=20)

# Pestaña 3: VERS
frame_vers = ttk.Frame(notebook)
notebook.add(frame_vers, text="VERS")

# Ejemplo de contenido para la pestaña 3
label3 = tk.Label(frame_vers, text="Aquí va VERS", font=("Arial", 16))
label3.pack(pady=20)

ventana.mainloop()
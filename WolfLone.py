import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # <-- Añade esta línea

# Crear ventana principal
ventana = tk.Tk()
ventana.title("WolfLone")

# Obtener la resolución de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Ajustar la ventana al tamaño de la pantalla
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

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

# Cargar y mostrar la imagen de fondo en frame_vers
imagen_fondo = Image.open("fondo_vers.jpg")  # Usa el nombre de tu archivo
imagen_fondo = imagen_fondo.resize((ancho_pantalla, alto_pantalla), Image.LANCZOS)
fondo_tk = ImageTk.PhotoImage(imagen_fondo)

label_fondo = tk.Label(frame_vers, image=fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
label_fondo.image = fondo_tk  # Evita que la imagen sea eliminada por el recolector de basura

# Puedes añadir más widgets encima si lo necesitas

ventana.mainloop()
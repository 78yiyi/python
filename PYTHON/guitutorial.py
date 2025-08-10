import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Mi primera ventana con tkinter")
ventana.geometry("1920x1080")  # Ancho x Alto
ventana.configure(bg="#ffcc99")
etiqueta = tk.Label(ventana, text="Hola Mundo", bg="black", fg="white", font=("Arial", 24))
etiqueta.pack(pady=20)  # Añade un margen vertical  

def mostrar_mensaje():
    etiqueta.config(text="¡Botón presionado!")
    messagebox.showinfo("Mensaje", "¡Has pulsado el botón!") 

boton = tk.Button(
    ventana,
    text="Haz clic aquí",
    command=mostrar_mensaje,
    bg="blue",
    fg="white",
    font=("Arial", 18)
)
boton.pack(pady=50)  # Añade un margen vertical

ventana.resizable(True, True)  # Permite redimensionar la ventana

def cerrar_ventana():
    print("La ventana se está cerrando...")
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Asocia el evento de cierre a la función personalizada  

ventana.mainloop()
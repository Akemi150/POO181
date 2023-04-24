import random
import tkinter as tk
from tkinter import messagebox
from LOGICA13 import *

# Función para generar y mostrar la contraseña
def mostrar_contraseña():
    longitud = int(longitud_entry.get()) if longitud_entry.get() else 8
    mayusculas = mayusculas_var.get()
    caracteres_especiales = caracteres_especiales_var.get()
    
    # Generar la contraseña
    contraseña = generar_contrasena(longitud, mayusculas, caracteres_especiales)
    
    # Mostrar la contraseña
    messagebox.showinfo("Contraseña generada", f"Su contraseña es: {contraseña}")
    
    # Comprobar la fortaleza de la contraseña
    puntos = comprobar_fortaleza(contraseña)
    mensaje = "Contraseña débil"
    if puntos >= 3:
        mensaje = "Contraseña fuerte"
    messagebox.showinfo("Fortaleza de la contraseña", mensaje)
    
# Crear la ventana de tkinter
ventana = tk.Tk()
ventana.title("GENERADOR PASSWORDS")
ventana.geometry("350x200")

# Crear los widgets
longitud_label = tk.Label(ventana, text="Longitud:")
longitud_entry = tk.Entry(ventana)
longitud_entry.insert(tk.END, "8")
mayusculas_var = tk.BooleanVar()
mayusculas_checkbutton = tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=mayusculas_var,bg="yellow")
caracteres_especiales_var = tk.BooleanVar()
caracteres_especiales_checkbutton = tk.Checkbutton(ventana, text="Incluir caracteres especiales", variable=caracteres_especiales_var,bg="orange")
generar_boton = tk.Button(ventana, text="Generar contraseña", command=mostrar_contraseña)


# Ubicar los widgets en la ventana
longitud_label.grid(row=0, column=0)
longitud_entry.grid(row=0, column=1)
mayusculas_checkbutton.grid(row=1, column=0, columnspan=2)
caracteres_especiales_checkbutton.grid(row=2, column=0, columnspan=2)
generar_boton.grid(row=3, column=0, columnspan=2, pady=10)

# Mostrar la ventana
ventana.mainloop()
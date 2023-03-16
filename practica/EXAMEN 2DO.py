
import tkinter as tk
import random

# Función para generar la matrícula
def generar_matricula():
    nombre = nombre_entry.get()
    apellido_paterno = ap_entry.get()
    apellido_materno = am_entry.get()
    fecha_nacimiento = fn_entry.get()
    grupo_salon = gs_entry.get()

    matricula = apellido_paterno[:2] + apellido_materno[:2] + nombre[:2] + fecha_nacimiento[-2:] + grupo_salon[:2]

    # Add 3 random numbers to the matricula
    matricula += str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

    matricula_label.config(text="Tu matrícula es: " + matricula)

# Creación de la ventana
ventana = tk.Tk()
ventana.title("Generador de Matrícula")

# Creación de los widgets
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_entry = tk.Entry(ventana)

ap_label = tk.Label(ventana, text="Apellido Paterno:")
ap_entry = tk.Entry(ventana)

am_label = tk.Label(ventana, text="Apellido Materno:")
am_entry = tk.Entry(ventana)

fn_label = tk.Label(ventana, text="Fecha de Nacimiento (DD/MM/AAAA):")
fn_entry = tk.Entry(ventana)

gs_label = tk.Label(ventana, text="Grupo de Salón:")
gs_entry = tk.Entry(ventana)

generar_button = tk.Button(ventana, text="Generar Matrícula", command=generar_matricula)

matricula_label = tk.Label(ventana, text="Tu matrícula aparecerá aquí")

# Posicionamiento de los widgets
nombre_label.grid(row=0, column=0)
nombre_entry.grid(row=0, column=1)

ap_label.grid(row=1, column=0)
ap_entry.grid(row=1, column=1)

am_label.grid(row=2, column=0)
am_entry.grid(row=2, column=1)

fn_label.grid(row=3, column=0)
fn_entry.grid(row=3, column=1)

gs_label.grid(row=4, column=0)
gs_entry.grid(row=4, column=1)

generar_button.grid(row=5, column=1)

matricula_label.grid(row=6, column=0, columnspan=2)

# Bucle principal de la aplicación
ventana.mainloop()



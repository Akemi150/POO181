#quiero una interfaz que genere una matricula





import tkinter as tk
import random

def matricula():
    nombre = nombre_entry.get()
    apellido_paterno = ap_entry.get()
    apellido_materno = am_entry.get()
    año_nacimiento = an_entry.get()
    año_curso = ac_entry.get()
    carrera = ca_entry.get()
    grupo= grupo_entry.get()


    matricula = nombre[0:1] + apellido_paterno[0:2] + apellido_materno[0:2] + año_nacimiento[0:2] + año_curso[0:2] + carrera[0:3] + grupo[0:2]
    
    matricula_label.config(text="Tu matrícula es: " + matricula)
    
    
ventana = tk.Tk()
ventana.title("Examen 2do Parcial: Matrícula")
nombre_label = tk.Label(ventana, text="Ingresa Nombre:", bg="purple")
nombre_entry = tk.Entry(ventana)
ap_label = tk.Label(ventana, text="Ingresa tu Apellido Paterno:", bg="pink")
ap_entry = tk.Entry(ventana)
am_label = tk.Label(ventana, text="Ingresa tu Apellido Materno:", bg="yellow")
am_entry = tk.Entry(ventana)
an_label = tk.Label(ventana, text="Ingresa tu Año de Nacimiento:", bg="green")
an_entry = tk.Entry(ventana)
ac_label = tk.Label(ventana, text="Ingresa tu Año de Curso:", bg="orange")
ac_entry = tk.Entry(ventana)
ca_label = tk.Label(ventana, text="Ingresa la Carrera que cursas:", bg="red")
ca_entry = tk.Entry(ventana)
grupo_label = tk.Label(ventana, text="Ingresa tu Grupo:", bg="blue")
grupo_entry = tk.Entry(ventana)

matricula_label = tk.Label(ventana, text="Tu matrícula es: ")


nombre_label.grid(row=0, column=0)
nombre_entry.grid(row=0, column=1)
ap_label.grid(row=1, column=0)
ap_entry.grid(row=1, column=1)
am_label.grid(row=2, column=0)
am_entry.grid(row=2, column=1)
an_label.grid(row=3, column=0)
an_entry.grid(row=3, column=1)
ac_label.grid(row=4, column=0)
ac_entry.grid(row=4, column=1)
ca_label.grid(row=5, column=0)  
ca_entry.grid(row=5, column=1)
grupo_label.grid(row=6, column=0)
grupo_entry.grid(row=6, column=1)
matricula_label.grid(row=8, column=0)


boton = tk.Button(ventana, text="Generar Matrícula", command=matricula)
boton.grid(row=10, column=0)


ventana.mainloop()



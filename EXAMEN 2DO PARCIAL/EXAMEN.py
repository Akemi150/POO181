



import tkinter as tk
import random

def matricula():
    nombre = nombre_entry.get()
    apellido_paterno = ap_entry.get()
    apellido_materno = am_entry.get()
    año_nacimiento = an_entry.get()
    grupo= grupo_entry.get()


    matricula_label.config(text="Tu matrícula es: " + matricula)
    
    
ventana = tk.Tk()
ventana.title("Examen 2do Parcial: Matrícula")
nombre_label = tk.Label(ventana, text="Ingresa Nombre:", bg="purple")
nombre_entry = tk.Entry(ventana)
ap_label = tk.Label(ventana, text="Ingresa tu Apellido Paterno:", bg="pink")
ap_entry = tk.Entry(ventana)
am_label = tk.Label(ventana, text="Ingresa tu Apellido Materno:", bg="yellow")
am_entry = tk.Entry(ventana)


                           
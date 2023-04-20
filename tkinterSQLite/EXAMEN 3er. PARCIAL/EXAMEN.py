
import sqlite3
import tkinter as tk
from tkinter import messagebox
from PedimentosBd import *

Ventana = tk.Tk()
Ventana.title("Pedimentos de Exportación")
Ventana.geometry("300x300")

# agregar un campo de entrada para el transporte
transporte_label = tk.Label(Ventana, text='Transporte:')
transporte_label.pack()
transporte_entry = tk.Entry(Ventana)
transporte_entry.pack()

# agregar un campo de entrada para la aduana
aduana_label = tk.Label(Ventana, text='Aduana:')
aduana_label.pack()
aduana_entry = tk.Entry(Ventana)
aduana_entry.pack()

# agregar un campo de entrada para el pedimento
pedimento_label = tk.Label(Ventana, text='Pedimento:')
pedimento_label.pack()
pedimento_entry = tk.Entry(Ventana)
pedimento_entry.pack()

# agregar un campo de entrada para la fecha
fecha_label = tk.Label(Ventana, text='Fecha:')
fecha_label.pack()
fecha_entry = tk.Entry(Ventana)
fecha_entry.pack()

# agregar un campo de entrada para el valor
valor_label = tk.Label(Ventana, text='Valor:')
valor_label.pack()
valor_entry = tk.Entry(Ventana)
valor_entry.pack()

#boton para guardar en la base de datos
def guardar():
    # obtener los datos de las entradas
    transporte = transporte_entry.get()
    aduana = aduana_entry.get()
    pedimento = pedimento_entry.get()
    fecha = fecha_entry.get()
    valor = valor_entry.get()
    # crear un objeto de la clase PedimentosBd
    pedimentos_bd = PedimentosBd()
    # guardar los datos en la base de datos
    pedimentos_bd.guardar_pedimento(transporte, aduana, pedimento, fecha, valor)
    # mostrar un mensaje de éxito
    messagebox.showinfo("Éxito", "El pedimento se guardó correctamente")


# iniciar el bucle principal de Tkinter
Ventana.mainloop()

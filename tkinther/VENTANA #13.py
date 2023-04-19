import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Login import Login


class Ventana(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Practica 13: AutoPassword")
        self.geometry("600x400")

        # Etiqueta de longitud
        self.lenlabel = tk.Label(text="Longitud de la contraseña:")
        self.lenlabel.pack()

        # Entry de Longitud
        self.entryLen = tk.Entry(self)
        self.entryLen.pack()

        # Checkbox de Mayusculas
        self.estado = tk.BooleanVar()
        self.checkboxm = tk.Checkbutton(self, text="Incluir mayuscula", variable=self.estado, onvalue=True, offvalue=False)
        self.checkboxm.pack()

        # Checkbox de caracteres especiales
        self.estado1 = tk.BooleanVar()
        self.checkboxes = tk.Checkbutton(self, text="Incluir caracteres especiales", variable=self.estado1, onvalue=True, offvalue=False)
        self.checkboxes.pack()

        # Boton de ingresar con la funcion de obtener los datos de los entry's, y mandarlos a la clase login
        self.button = tk.Button(self, text="Generar Contraseña", command=self.on_button)
        self.button.pack()

    # Función para el botón
    def on_button(self):
        # se crea el objeto con los gets de los entry's
        seg = Login("email", "password")
        seg.generarContraseña(int(self.entryLen.get()), self.estado.get(), self.estado1.get())
        gen = Login("email", "password")
        gen.generarContraseña(int(self.entryLen.get()), self.estado.get(), self.estado1.get())

        print(self.entryLen.get())
        print(self.estado.get())
        print(self.estado1.get())

ventana = Ventana()
ventana.mainloop()
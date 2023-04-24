import tkinter as tk
from tkinter import messagebox
from LOGICA import *

class RomanConverter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("EXAMEN FINAL 2do. PARCIAL")
        self.master.geometry("400x200")
        self.pack()
        self.creación_widgets()

    def creación_widgets(self):
        self.roman_label = tk.Label(self, text="Ingresa Números Romanos:",bg="PURPLE")
        self.roman_label.pack()
        self.roman_entry = tk.Entry(self)
        self.roman_entry.pack()

        self.arabic_label = tk.Label(self, text="Ingresa Numeros Árabigos:",bg="PINK")
        self.arabic_label.pack()
        self.arabic_entry = tk.Entry(self)
        self.arabic_entry.pack()

        #CONVERSION DE ROMANOS A ARABIGOS Y VICEVERSA
        self.roman_to_arabic = tk.Button(self, text="Convertir de Romanos a Arábigos", command=self.conversion_arabe)
        self.roman_to_arabic.pack()

        self.arabic_to_roman = tk.Button(self, text="Convertir de Arábigos a Romanos", command=self.conversion_romano)
        self.arabic_to_roman.pack()

        #Mensaje de error
        self.error_label = tk.Label(self, text="", fg="red")
        self.error_label.pack()

    def conversion_arabe(self):
     roman_numeral = self.roman_entry.get()
     if not roman_numeral:
        self.error_label.config(text="Por favor ingresa un número romano")
        return
     arabic_numeral = romano_arabe(roman_numeral.upper())
     if arabic_numeral is None:
        self.error_label.config(text="El número romano ingresado no existe")
        return
     if arabic_numeral < 1 or arabic_numeral > 50:
        self.error_label.config(text="Los números romanos deben estar entre 1 y 50")
        return
     self.arabic_entry.delete(0, tk.END)
     self.arabic_entry.insert(0, str(arabic_numeral))
     self.error_label.config(text="")

    def conversion_romano(self):
        arabic_numeral = self.arabic_entry.get()
        if not arabic_numeral:
            self.error_label.config(text="Por favor ingresa un número arábigo")
            return
        try:
            arabic_numeral = int(arabic_numeral)
            if arabic_numeral < 1 or arabic_numeral > 50:
                self.error_label.config(text="Los números arábigos deben estar entre 1 y 50")
                return
            roman_numeral = arabe_romano(arabic_numeral)
        except ValueError:
            self.error_label.config(text="Numeros Arábigos Incorrectos")
            return
        self.roman_entry.delete(0, tk.END)
        self.roman_entry.insert(0, roman_numeral)
        self.error_label.config(text="")

root = tk.Tk()
app = RomanConverter(master=root)
app.mainloop()

from tkinter import Tk,Frame,Button
import tkinter as tk

ventana= Tk()
ventana.title(" Practica 14: CAJA ")
ventana.geometry("350x350")

Seccion1=Frame(ventana,bg="#e6ccff")
Seccion1.pack(expand=True,fill='both')

SeleccionarMenu= Button(Seccion1, text="MENU DE OPERACIONES" ,fg="#000d1a",command="    ")
SeleccionarMenu.place(x=60, y=60)


        
ventana.mainloop()
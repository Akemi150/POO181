
from tkinter import *
from LOGICA import *    
import tkinter as tk

axc= logica()

def ejecutaVal():
    axc.validarCredenciales(var1.get(),var2.get())    
    
Ventana= Tk()
Ventana.title("Login")
Ventana.geometry("300x150")

Seccion1= Frame(Ventana)
Seccion1.pack(expand= True, fill= 'both')

titulo= Label(Seccion1,text="Login POO", bg="black", fg="white", font=("Helvetica",18)).pack()

var1 = tk.StringVar()
lblContra= Label(Seccion1,text="Correo: ").pack()
txtCorreo= Entry(Seccion1,textvariable=var1,takefocus=True).pack()

var2 = tk.StringVar()
lblContra= Label(Seccion1,text=" Contraseña: ").pack()
txtContra= Entry(Seccion1,show="++", textvariable=var2).pack()

botonAcceso= Button(Seccion1, text="Acceder",bg="green", command=ejecutaVal)
botonAcceso.pack()

Ventana.mainloop()








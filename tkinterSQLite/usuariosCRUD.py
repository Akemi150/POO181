from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

Pestaña1= ttk.Frame(panel)
Pestaña2= ttk.Frame(panel)
Pestaña3= ttk.Frame(panel)
Pestaña4= ttk.Frame(panel)

# PESTAÑA1: FORMUALRIO DE USUARIOS

titulo= Label(Pestaña1,text="Registro de Usuarios", fg="purple", font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(Pestaña1, text="Nombre: ").pack()
txtNom= Entry(Pestaña1, textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(Pestaña1, text="Correo: ").pack()
txtCor= Entry(Pestaña1, textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(Pestaña1, text="Contraseña: ").pack()
txtCon= Entry(Pestaña1, textvariable=varCon).pack()

btnGuardar= Button(Pestaña1, text="Guardar Usuario").pack()

panel.add(Pestaña1, text="Formulario Usuarios")
panel.add(Pestaña2, text="Buscar Usuarios")
panel.add(Pestaña3, text="Consultar Usuarios")
panel.add(Pestaña4, text="Actualizar Usuarios")

Ventana.mainloop()
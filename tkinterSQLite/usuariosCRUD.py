from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *   #1. Presentamos los archivos Controlador Vista
from tkinter import messagebox

#2. Creamos 1 objeto de la Clase ControladorBD
controlador= controladorBD()

#3. Función para disparar el botón
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

#4. FUNCION PARA DISPARAR EL BOTON BUSQUEDA
def ejecutaSelectU():
    Usuario= controlador.consultarUsuario(varBus.get())
    for usu in Usuario:
      cadena= str(usu[0]) + " " + usu[1] + " " + usu[2] + " " + str(usu[3])

    if(Usuario):
      print(cadena)
    else:
        messagebox.showinfo("No encontrado","Ese usuario no existe en la base de datos")
        
def ejecutaSelectU():
    Usuario = controlador.consultarUsuario(varBus.get())
    if Usuario:
        cadena = "ID\tNombre\tCorreo\tContraseña\n"
        for usu in Usuario:
            cadena += f"{usu[0]}\t{usu[1]}\t{usu[2]}\t{usu[3]}\n"
        textEnc.delete('1.0', END)
        textEnc.insert('1.0', cadena)
    else:
        messagebox.showinfo("No encontrado","Ese usuario no existe en la base de datos")
   
#una consulta a la base de datos para importar TODOS LOS USUARIOS de en la Tabla Registrados a la interfaz de Python  

def ejecutaConsulta():
    Usuarios= controlador.consultarUsuarios()
    cadena= "ID\tNombre\tCorreo\tContraseña\n"
    for usu in Usuarios:
        cadena += f"{usu[0]}\t{usu[1]}\t{usu[2]}\t{usu[3]}\n"
    textEnc.delete('1.0', END)
    textEnc.insert('1.0', cadena)

#Creamos la ventana

Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("800x300")

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

btnGuardar= Button(Pestaña1, text="Guardar Usuario",command=ejecutaInsert).pack()

# PESTAÑA2: BUSCAR USUARIO

titulo2= Label(Pestaña2,text="Buscar Usuario", fg="red", font=("Modern",18)).pack()

varBus= tk.StringVar()
lblid= Label(Pestaña2, text="Identificador de Usuario: ").pack()
txtid= Entry(Pestaña2, textvariable=varBus).pack()
btnBus= Button(Pestaña2, text="Buscar",command=ejecutaSelectU).pack()

subBus=Label(Pestaña2,text="Encontrado", fg="blue", font=("Modern",15))
textEnc= tk.Text(Pestaña2,height=5,width=52)
textEnc.pack()

# PESTAÑA3: CONSULTAR USUARIOS

titulo3= Label(Pestaña3,text="Consultar Usuarios", fg="green", font=("Modern",18)).pack()
btnCons= Button(Pestaña3, text="Consultar",command=ejecutaConsulta).pack()

subCons=Label(Pestaña3,text="Encontrados", fg="blue", font=("Modern",15))
textEnc= tk.Text(Pestaña3,height=5,width=52)
textEnc.pack()




panel.add(Pestaña1, text="Formulario Usuarios")
panel.add(Pestaña2, text="Buscar Usuarios")
panel.add(Pestaña3, text="Consultar Usuarios")
panel.add(Pestaña4, text="Actualizar Usuarios")

Ventana.mainloop()
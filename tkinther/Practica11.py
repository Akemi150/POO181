
from tkinter import Tk,Frame,Button,messagebox

#4.Función de mensajes para el botón

def mostrarMensaje():
    messagebox.showinfo("Aviso", "Este mensaje es para informar algo")
    messagebox.showerror("Error:","Todo fallo con éxito")
    print(messagebox.askquestion("Pregunta:","El o ella jugo con tu corazón"))

#5. Función para agregar botones:
def agregarBoton():
    BotonAmarillo.config(text="+", bg="#cc9900")
    BotonNuevo= Button(Seccion3,text="Boton Nuevo")
    BotonNuevo.pack()
    
    
#1. Crear ventana
ventana= Tk()
ventana.title(" Practica 11:Frames ")
ventana.geometry("600x400")

#2. Definimos Secciones de la ventana
Seccion1=Frame(ventana,bg="#e6ccff")
Seccion1.pack(expand=True,fill='both')

Seccion2=Frame(ventana,bg="#b3ecff")
Seccion2.pack(expand=True,fill='both')

Seccion3=Frame(ventana,bg="#ffffcc")
Seccion3.pack(expand=True,fill='both')

#3. Botones
BotonAzul= Button(Seccion1, text="Botón Azul" ,fg="#000d1a",command=mostrarMensaje )
BotonAzul.place(x=60, y=60)

BotonRojo= Button(Seccion2, text="Botón Rojo" ,fg="#000d1a")
BotonRojo.grid(row=0, column=0)


BotonNegro= Button(Seccion2, text="Botón Negro" ,fg="#000d1a", bg="#5c5c8a")
BotonNegro.grid(row=1, column=0)
BotonNegro.place(x=60, y=60)

BotonAmarillo= Button(Seccion3, text="Botón Amarillo" ,bg="#e6e600",command= agregarBoton)
BotonAmarillo.pack()


#Main de ejecución de la ventana (ultima línea del archivo)
ventana.mainloop()
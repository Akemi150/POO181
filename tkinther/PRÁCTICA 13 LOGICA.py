
from tkinter import Tk,Frame,Button,messagebox



def mostrarMensaje():
    messagebox.showinfo("Aviso", "Este mensaje es para informar algo")
    messagebox.showerror("Error:","Todo fallo con éxito")
    print(messagebox.askquestion("Pregunta:","El o ella jugo con tu corazón"))

    
ventana= Tk()
ventana.title(" Practica 13 Tkinter y POO ")
ventana.geometry("600x400")


Seccion1=Frame(ventana,bg="#e6ccff")
Seccion1.pack(expand=True,fill='both')


Contraseña= Button(Seccion1, text="Generar Contraseña con una longitud de 8 caracteres" ,fg="#000d1a",command=mostrarMensaje )
Contraseña.place(x=60, y=60)


ventana.mainloop()




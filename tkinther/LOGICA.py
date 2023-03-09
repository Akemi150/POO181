
from tkinter import messagebox

class logica:
    
    def __init__(self):
        self.__correoC= "iiguerra@outlook.com"
        self.__contraC="la2b3c4d"
        
    def validarCredenciales(self,correo,contra):
        if(correo == "" or contra == ""):
            messagebox.showwarning("Cuidado","Usuario y contraseña debe contener algo")
        else:
            if(self.__correoC == correo and self.__contraC == contra):
                messagebox.showerror("Error","Revisa tus credenciales")
                    
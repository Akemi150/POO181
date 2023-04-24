from tkinter import *
from tkinter import messagebox
import random
 

class Cuenta:
    def __init__(self, Numero, Titular, Edad, Saldo):
        self.Numero = Numero
        self.Titular = Titular
        self.Edad = Edad
        self.Saldo = Saldo
        
    def __str__(self):
        return "No. Cuenta: {}, Titular: {}, Edad: {}, Saldo: {}".format(
            self.Numero, self.Titular, self.Edad, self.Saldo)
    
    def __repr__(self):
        return "Cuenta({}, {}, {}, {})".format(
            self.Numero, self.Titular, self.Edad, self.Saldo)
    
    def __eq__(self, other):
        if isinstance(other, Cuenta):
            return self.Numero == other.Numero
        else:
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)


class Caja:
    def __init__(self):
        self.cuentas = []
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        
    def consultar_Saldo(self, Numero):
        for cuenta in self.cuentas:
            if cuenta.Numero == Numero:
                return cuenta.Saldo
        return None
        
    def ingresar_efectivo(self, Numero, Cantidad):
        for cuenta in self.cuentas:
            if cuenta.Numero == Numero:
                cuenta.Saldo += Cantidad
                return True
        return False
        
    def retirar_efectivo(self, Numero, Cantidad):
        for cuenta in self.cuentas:
            if cuenta.Numero == Numero:
                if cuenta.Saldo >= Cantidad:
                    cuenta.Saldo -= Cantidad
                    return True
                else:
                    return False
        return False
        
    def depositar_a_otra_cuenta(self, Numero, Cantidad, Numero2):
        for cuenta in self.cuentas:
            if cuenta.Numero == Numero:
                if cuenta.Saldo >= Cantidad:
                    cuenta.Saldo -= Cantidad
                    for cuenta2 in self.cuentas:
                        if cuenta2.Numero == Numero2:
                            cuenta2.Saldo += Cantidad
                            return True
                else:
                    return False
        return False
    

class NuevaCuenta(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Nueva Cuenta")
        self.grab_set()
        
        self.Numero = random.randint(1000, 9999)
        self.titular = StringVar()
        self.edad = StringVar()
        
        Label(self, text="No. Cuenta: {}".format(self.Numero)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        Label(self, text="Titular: ").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        Entry(self, textvariable=self.titular).grid(row=1, column=1, padx=5, pady=5)
        Label(self, text="Edad: ").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        Entry(self, textvariable=self.edad).grid(row=2, column=1, padx=5, pady=5)

        Button(self, text="Crear", command=self.crear).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
    def crear(self):
        if self.titular.get() == "" or self.edad.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            self.parent.caja.agregar_cuenta(Cuenta(self.Numero, self.titular.get(), int(self.edad.get()), 0))
            messagebox.showinfo("Información", "Cuenta creada con éxito")
            self.destroy()
    
    
            
class Formulario(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("CAJA POPULAR: PRÁCTICA 14")
        self.geometry("300x300")
        self.caja = Caja()
        
        
        self.Numero = StringVar()
        self.Cantidad = StringVar()
        self.Numero2 = StringVar()
        
        Label(self, text="No. Cuenta: ").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.Numero).grid(row=0, column=1, padx=5, pady=5)
        
        Label(self, text="Cantidad: ").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.Cantidad).grid(row=1, column=1, padx=5, pady=5)
        
        Label(self, text="No. Cuenta 2: ").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.Numero2).grid(row=2, column=1, padx=5, pady=5)
        
        Button(self, text="Consultar Saldo", command=self.consultar_Saldo).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Ingresar Efectivo", command=self.ingresar_efectivo).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Retirar Efectivo", command=self.retirar_efectivo).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Depositar a otra cuenta", command=self.depositar_a_otra_cuenta).grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Nueva Cuenta", command=self.nueva_cuenta).grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Ver Todas las Cuentas", command=self.ver_todas).grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        
        
    def consultar_Saldo(self):
        if self.Numero.get() == "":
            messagebox.showerror("Error", "Debe llenar el campo No. Cuenta")
        else:
            Saldo = self.caja.consultar_Saldo(int(self.Numero.get()))
            if Saldo is None:
                messagebox.showerror("Error", "No existe la cuenta")
            else:
                messagebox.showinfo("Información", "El Saldo de la cuenta es: {}".format(Saldo))
            
    def ingresar_efectivo(self):
        if self.Numero.get() == "" or self.Cantidad.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.ingresar_efectivo(int(self.Numero.get()), float(self.Cantidad.get())):
                messagebox.showinfo("Información", "Efectivo ingresado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
                
    def retirar_efectivo(self):

        if self.Numero.get() == "" or self.Cantidad.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.retirar_efectivo(int(self.Numero.get()), float(self.Cantidad.get())):
                messagebox.showinfo("Información", "Efectivo retirado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
                
    def depositar_a_otra_cuenta(self):

        if self.Numero.get() == "" or self.Cantidad.get() == "" or self.Numero2.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.depositar_a_otra_cuenta(int(self.Numero.get()), float(self.Cantidad.get()), int(self.Numero2.get())):
                messagebox.showinfo("Información", "Efectivo depositado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
    
    def nueva_cuenta(self):
        NuevaCuenta(self)
    
    def ver_todas(self):
        cuentas = [str(cuenta) for cuenta in self.caja.cuentas]
        if len(cuentas) == 0:
            messagebox.showinfo("No hay cuentas registradas")
        else:
            messagebox.showinfo("Cuentas", "\n".join(cuentas))
 

if __name__ == "__main__":
    app = Formulario()
    app.mainloop()
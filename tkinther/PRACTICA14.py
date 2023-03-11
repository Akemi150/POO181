
import tkinter as tk
from tkinter import ttk
class GreetingFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()
        
        self.greet_button = ttk.Button(
            self, text="Ingresa tu Nombre", command=self.say_hello)
        self.greet_button.pack()
        
        self.greet_label = ttk.Label(self)
        self.greet_label.pack()
    
    def say_hello(self):
        self.greet_label["text"] = \
            "¡Hola Bienvenid@, {}!".format(self.name_entry.get())

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Panel de pestañas en Tcl/Tk")
        
        self.notebook = ttk.Notebook(self)
        
        self.greeting_frame = GreetingFrame(self.notebook)
        self.notebook.add(
            self.greeting_frame, text="Menú Principal", padding=10)
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()
    
    def CrearVentana():
        Ventana = tk.Toplevel(app)
        
    app = tk.Tk()
    ButtonMenuOperaciones = tk.Button(app,text="Menu de Operaciones", command=)
    ButtonMenuOperaciones.pack()
      
        
        
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()       
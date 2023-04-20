import tkinter as tk
import sqlite3
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("Exportaciones")
        
        self.transport_label = tk.Label(master, text="Transporte:")
        self.transport_label.grid(row=0, column=0)
        
        self.transport_entry = tk.Entry(master)
        self.transport_entry.grid(row=0, column=1)
        
        self.aduana_label = tk.Label(master, text="Aduana:")
        self.aduana_label.grid(row=1, column=0)
        
        self.aduana_entry = tk.Entry(master)
        self.aduana_entry.grid(row=1, column=1)
        
        self.add_button = tk.Button(master, text="Agregar", command=self.add_pedimento)
        self.add_button.grid(row=2, column=0)
        
        self.delete_button = tk.Button(master, text="Eliminar", command=self.delete_pedimento)
        self.delete_button.grid(row=2, column=1)
        
        self.consulta_button = tk.Button(master, text="Consultar", command=self.consulta_aduana)
        self.consulta_button.grid(row=3, column=0)
        
        self.view_button = tk.Button(master, text="Ver pedimentos", command=self.view_pedimentos)
        self.view_button.grid(row=3, column=1)
        
        # Conexión a la base de datos
        self.conn = sqlite3.connect("BaseAkemi.db")
        self.c = self.conn.cursor()
        
        # Creación de la tabla si no existe
        self.c.execute("""CREATE TABLE IF NOT EXISTS TBPedimentos (
                            IDExpo INTEGER PRIMARY KEY AUTOINCREMENT,
                            Transporte TEXT,
                            Aduana TEXT
                            )""")
        self.conn.commit()
    
    def add_pedimento(self):
        # Inserta un nuevo pedimento en la base de datos con los valores de los campos
        self.c.execute("INSERT INTO TBPedimentos (Transporte, Aduana) VALUES (?, ?)", 
                       (self.transport_entry.get(), self.aduana_entry.get()))
        self.conn.commit()
        
        # Borra los valores de los campos después de insertar el pedimento
        self.transport_entry.delete(0, tk.END)
        self.aduana_entry.delete(0, tk.END)
    
    def delete_pedimento(self):
      try:
        # Obtener el índice del elemento seleccionado en la lista de pedimentos
        selected_item = self.pedimentos_listbox.curselection()[0]
        item_text = self.pedimentos_listbox.get(selected_item)
        if ":" not in item_text:
            raise ValueError("El elemento seleccionado no tiene el formato esperado")
        id_expo = int(item_text.split(":")[1])
        
        
        # Eliminar el pedimento de la base de datos
        self.c.execute("DELETE FROM TBPedimentos WHERE IDExpo=?", (id_expo,))
        self.conn.commit()
        
        # Actualizar la lista de pedimentos
        self.view_pedimentos()
      except IndexError:
             messagebox.showinfo("Error", "Seleccione un pedimento para eliminar")
      except ValueError as e:
            messagebox.showinfo("Error", str(e))
            
            print(self.pedimentos_listbox.curselection())
            selected_item = self.pedimentos_listbox.curselection()[0]


    
    def consulta_aduana(self):
        # Consulta los pedimentos por aduana
        aduana = self.aduana_entry.get()
        self.c.execute("SELECT * FROM TBPedimentos WHERE Aduana=?", (aduana,))
        rows = self.c.fetchall()
        
        if len(rows) == 0:
            tk.messagebox.showinfo("Error", "No hay pedimentos registrados para esta aduana")
        else:
            pedimentos = ""
            for row in rows:
                pedimentos += f"ID: {row[0]}, Transporte: {row[1]}, Aduana: {row[2]}\n"
        # Muestra los resultados en una ventana nueva
        if pedimentos != "":
            results_window = tk.Toplevel(self.master)
            results_window.title("Resultados de consulta")
            
            results_label = tk.Label(results_window, text=pedimentos)
            results_label.pack()
    
    def view_pedimentos(self):
        # Obtiene todos los pedimentos de la base de datos y los muestra en una lista
        self.c.execute("SELECT * FROM TBPedimentos")
        rows = self.c.fetchall()
        pedimentos = [f"ID: {row[0]}, Transporte: {row[1]}, Aduana: {row[2]}" for row in rows]
        
        if len(pedimentos) == 0:
            pedimentos.append("No hay pedimentos registrados")
        
        if hasattr(self, "pedimentos_listbox"):
            self.pedimentos_listbox.destroy()
        
        self.pedimentos_listbox = tk.Listbox(self.master, width=50)
        
        for i, pedimento in enumerate(pedimentos):
            self.pedimentos_listbox.insert(i, pedimento)
        
        self.pedimentos_listbox.grid(row=4, column=0, columnspan=2)

root = tk.Tk()
root.title("Exportaciones")
root.geometry("420x300")
app = App(root)
root.mainloop()

# Cerrar la conexión a la base de datos al salir de la aplicación
app.conn.close()
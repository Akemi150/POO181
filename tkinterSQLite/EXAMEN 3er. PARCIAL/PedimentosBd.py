from tkinter import messagebox
import sqlite3



#metodo para crear la conexion
def PedimentosBD():
    try:
        conexion= sqlite3.connect("/Users/akemi150/Documents/GitHub/POO181/tkinterSQLite/EXAMEN 3er. PARCIAL/EXAMEN EXPORTACIONES.db")
        print("Conectado a la BD")
        return conexion 
    except sqlite3.OperationalError:
        print("No se pudo conectar")
    
# función para agregar un nuevo pedimento a la tabla
def agregar_pedimento():
    transporte = transporte_entry.get()
    aduana = aduana_entry.get()
    conn.execute("INSERT INTO TBPedimentos (Transporte, Aduana) VALUES (?, ?)", (transporte, aduana))
    conn.commit()
    status_label.config(text="Pedimento agregado")

# función para eliminar un pedimento de la tabla
def eliminar_pedimento():
    id_expo = id_expo_entry.get()
    conn.execute("DELETE FROM TBPedimentos WHERE IDExpo = ?", (id_expo,))
    conn.commit()
    status_label.config(text="Pedimento eliminado")

# función para buscar pedimentos por aduana
def buscar_pedimentos():
    aduana = aduana_entry.get()
    cursor = conn.execute("SELECT * FROM TBPedimentos WHERE Aduana = ?", (aduana,))
    result = cursor.fetchall()
    if result:
        status_label.config(text="")
        for row in result:
            pedimentos_listbox.insert(tk.END, row)
    else:
        status_label.config(text="No se encontraron pedimentos para esta aduana")
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
    
#metodo para consultar todos los pedimentos
def consultarPedimentos():

    #1. PREPARAR UNA CONEXION
    Conx= PedimentosBD()

    try:
        #2. PREPARAR LO NECESARIO
        cursor= Conx.cursor()
        selectQry= "Select * from TBPedimentos"

        #3. EJECUTAR Y GUARDAR LA CONSULTA
        cursor.execute(selectQry)
        rsPedimentos= cursor.fetchall()

        return rsPedimentos

    except sqlite3.OperationalError:
        print("Error Consulta")
        
#Metodo para Guardar Pedimentos

def guardarPedimento(Transp,Adu):
        
        #1. Usamos una conexion
        Conx= PedimentosBD()
        
        #2. Validar parametros Vacios
        if(Transp == "" or Adu == ""):
            messagebox.showwarning("Aguas", "Formulario Incompleto")
        else:
            
            #3. Preparamos Cursor,Datos,QuerySQL
            Cursor= Conx.cursor()  
            Datos=(Transp,Adu)
            qrInsert= "insert into TBPedimentos(Transporte,Aduana) values(?,?)" 
            
            #4. Ejecutar Insert y cerramos Conexión
            Cursor.execute(qrInsert,Datos) 
            Conx.commit()
            
#Metodo para buscar pedimentos por aduana

def buscarPedimentos(Adu):
            
            #1. Usamos una conexion
            Conx= PedimentosBD()
            
            #2. Validar parametros Vacios
            if(Adu == ""):
                messagebox.showwarning("Aguas", "Formulario Incompleto")
            else:
                
                #3. Preparamos Cursor,Datos,QuerySQL
                Cursor= Conx.cursor()  
                Datos=(Adu)
                qrInsert= "Select * from TBPedimentos where Aduana=?" 
                
                #4. Ejecutar Insert y cerramos Conexión
                Cursor.execute(qrInsert,Datos) 
                Conx.commit()



from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    # Metodo para crear conexiones
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("/Users/akemi150/Documents/GitHub/POO181/tkinterSQLite/DBUsuarios.db")
            print("Conectado a la BD")
            return conexion 
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
            
    #Metodo para consultar todos los usuarios
    def consultarUsuarios(self):
        #1. PREPARAR UNA CONEXION
        Conx= self.conexionBD()
        
        try:
            #2. PREPARAR LO NECESARIO
            cursor= Conx.cursor()
            selectQry= "Select * from TBRegistrados"
            
            #3. EJECUTAR Y GUARDAR LA CONSULTA
            cursor.execute(selectQry)
            rsUsuarios= cursor.fetchall()
            
            return rsUsuarios
            
        except sqlite3.OperationalError:
            print("Error Consulta")

    
    #Metodo para Guardar Usuarios
    def guardarUsuario(self,Nom,Cor,Con):
        
        #1. Usamos una conexion
        Conx= self.conexionBD()
        
        #2. Validar parametros Vacios
        if(Nom == "" or Cor == "" or Con == ""):
            messagebox.showwarning("Aguas", "Formulario Incompleto")
        else:
            
            #3. Preparamos Cursor,Datos,QuerySQL
            Cursor= Conx.cursor()  
            ConH= self.encriptarCon(Con)
            Datos=(Nom,Cor,ConH)
            qrInsert= "insert into TBRegistrados(nombre,correo,contra) values(?,?,?)" 
            
            #4. Ejecutar Insert y cerramos Conexión
            Cursor.execute(qrInsert,Datos) 
            Conx.commit()
            Conx.close
            messagebox.showinfo("Éxito", "Usuario Guardado")
     


    # Método para encriptar Contraseñas    
    def encriptarCon(self,Con):
            ConPlana= Con
            
            
            #Preparamos con en bytes y la SAL
            ConPlana= ConPlana.encode()    #Convertimos con a bytes
            Sal= bcrypt.gensalt()
            
            #Encryptamos la contraseña
            ConHa= bcrypt.hashpw(ConPlana, Sal)
            print(ConHa)
            return ConHa


        
    # MÉTODO PARA BUSCAR 1 USUARIO
         
    def consultarUsuario(self,id):
        #1. PREPARAR UNA CONEXION
        Conx= self.conexionBD()

        #2. VERIFICAR SI ID CONTIENE ALGO
        if(id == ""):
            messagebox.showwarning("Cuidado","Id vacio escribe algo válido")
        else:
             try:
                 #3.PREPARAR LO NECESARIO
                 cursor= Conx.cursor()
                 selectQry= "Select * from TBRegistrados where id="+id
                 
                 #4.EJECUTAR Y GUARDAR LA CONSULTA
                 cursor.execute(selectQry)
                 rsUsuario= cursor.fetchall()
                 
                 return rsUsuario
                 
             except sqlite3.OperationalError:
                 print("Error Consulta")
                 

                 


class Personaje: 
    
#ATRIBUTOS DEL PERSONAJE

especie = "Humano"
nombre = "Fenix"
altura = 1.90

#Metodos Personaje

def correr(self, status):
    if(status):
        print("El personaje "+ self.nombre + "esta corriendo" )
    else:
        print("El personaje "+ self.nombre + "se detuvo" )    
        
def lanzarGranada (self):
    print ("Se lanzo Granada ")   

def recargarArma(self, munciones): 
    cargador= 5
    cargador = cargador + munciones     
    print("El arma tiene ahora "+ cargador +"balas")

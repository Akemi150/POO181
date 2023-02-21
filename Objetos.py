
#1. Importar la clase
from Personaje import *


#2. Instanciar un objeto
Heroe = Personaje()


#3. Acceder a sus atributos
print("Atributos Personaje")
print ("El personaje pertenece a la raza: "+ Heroe.especie)
print ("Se llama : "+ Heroe.nombre)
print ("Mide : "+ str(Heroe.altura) + "Metros")
print("")

print("Metodos Personaje")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(68)
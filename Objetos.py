
#1. Importar la clase
from Personaje import *


#2. Solicitar los atributos para el objeto 
print("")
print("### Solicitud de datos Heroe ###")
espH= input("Escribe la esepcie del Heroe")
nomH= input("Escribe el nombre del Heroe")
altH= float(input("Escribe la altura del Heroe"))
cargaH= (int(input("¿Cuántas balas se recargaran al Heroe?")))

print("")
print("### Solicitud de datos del Villano ###")
espV= input("Escribe la esepcie del Villano ")
nomV= input("Escribe el nombre del Villano")
altV= float(input("Escribe la altura del Villano"))
cargaV= (int(input("¿Cuántas balas se recargaran al Villano?")))



#3. Creamos 2 objetos
Heroe= Personaje(espH, nomH, altH)
Villano= Personaje(espV, nomV, altV)


Heroe.setNombre("Pepe pecas")


#4. Acceder a atributos y metodos del cada OBJ

print("")
print("Atributos y Metodos del Heroe ##")
print ("El personaje pertenece a la raza: "+ Heroe.getEspecie())
print ("Se llama : "+ Heroe.getNombre())
print ("Mide : "+ str(Heroe.getAltura( )) + "Metros")
print("")

print("Metodos Personaje")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)
Heroe.__pensar()

print("Atributos y Metodos del Villano ##")
print ("El personaje pertenece a la raza: "+ Villano.getEspecie())
print ("Se llama : "+ Villano.getNombre())
print ("Mide : "+ str(Villano.getAltura()) + "Metros")
print("")

print("Metodos Personaje")
Villano.correr(True)
Villano.lanzarGranada()
Villano.recargarArma(cargaH)


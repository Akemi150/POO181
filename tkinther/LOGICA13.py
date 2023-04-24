from tkinter import messagebox
import random
import string

# Función para generar la contraseña
def generar_contrasena(longitud=8, mayusculas=False, caracteres_especiales=False):
    # Selección de caracteres permitidos
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if caracteres_especiales:
        caracteres += string.punctuation
    
    # Generación de la contraseña
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

# Función para comprobar la fortaleza de la contraseña
def comprobar_fortaleza(contraseña):
    puntos = 0
    if any(c.isupper() for c in contraseña):
        puntos += 1
    if any(c.islower() for c in contraseña):
        puntos += 1
    if any(c.isdigit() for c in contraseña):
        puntos += 1
    if any(c in string.punctuation for c in contraseña):
        puntos += 1
    return puntos
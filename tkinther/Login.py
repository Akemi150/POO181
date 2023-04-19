import string
import random

class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def checarSeguridad(self, longitud):
        if longitud < 8:
            print("La longitud de la contraseña es muy corta")
        elif longitud >= 8 and longitud <= 8:
            print("La contraseña es medianamente segura")
        else:
            print("La contraseña es muy segura")

    def generarContraseña(self, longitud, incluirMayuscula, incluirCaracterEspecial):
        letras_minusculas = string.ascii_lowercase
        letras_mayusculas = string.ascii_uppercase
        digitos = string.digits
        caracteres_especiales = string.punctuation

        caracteres = letras_minusculas + digitos
        if incluirMayuscula:
            caracteres += letras_mayusculas
        if incluirCaracterEspecial:
            caracteres += caracteres_especiales

        contraseña_generada = ''.join(random.choice(caracteres) for i in range(longitud))
        print(f"La contraseña generada es: {contraseña_generada}")
        return contraseña_generada

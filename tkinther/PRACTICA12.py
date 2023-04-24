import tkinter as tk
import tkinter.messagebox as msg

# Definir los datos de usuario permitidos
usuarios = {
    "usuario1@gmail.com": "contraseña1",
    "usuario2@hotmail.com": "contraseña2",
}

# Función para verificar las credenciales del usuario
def verificar_datos():
    correo = correo_entry.get()
    contraseña = contraseña_entry.get()
    if correo in usuarios and usuarios[correo] == contraseña:
        msg.showinfo("Bienvenido", "Ha iniciado sesión correctamente.")
    else:
        mensaje_label.config(text="Por favor revise sus datos e intente de nuevo.",bg="red")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Práctica 12: Login con Tkinter")
ventana.geometry("350x192")

# Crear los widgets
mensaje_label = tk.Label(ventana, text="Ingrese sus datos")
correo_label = tk.Label(ventana, text="Correo electrónico:", bg="purple")
correo_entry = tk.Entry(ventana)
contraseña_label = tk.Label(ventana, text="Contraseña:", bg="pink")
contraseña_entry = tk.Entry(ventana, show="*")
iniciar_sesion_boton = tk.Button(ventana, text="Iniciar sesión", command=verificar_datos)

# Ubicar los widgets en la ventana
mensaje_label.grid(row=0, column=0, columnspan=2)
correo_label.grid(row=1, column=0)
correo_entry.grid(row=1, column=1)
contraseña_label.grid(row=2, column=0)
contraseña_entry.grid(row=2, column=1)
iniciar_sesion_boton.grid(row=3, column=0, columnspan=2, pady=10)

# Mostrar la ventana
ventana.mainloop()

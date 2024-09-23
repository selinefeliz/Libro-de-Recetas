# Importaciones 
import tkinter
import customtkinter as ctk
from CTkMenuBar import *

# Configuración del modo de apariencia
ctk.set_appearance_mode("System")  # Establece el modo de color del sistema
ctk.set_default_color_theme("blue")  # Establece el tema de color predeterminado

# Crear la ventana principal
app = ctk.CTk()  # Puedes cambiar el nombre de "app"
app.geometry("600x540")  # Establecer el tamaño de la ventana
app.title("Recetas")


# Función para insertar receta
def insertarReceta():
    # Ocultar la ventana principal
    app.withdraw()

    # Crear una nueva ventana
    nueva_ventana = ctk.CTkToplevel(app)
    nueva_ventana.geometry("600x540")
    nueva_ventana.title("Insertar receta")
    
    # Crear y ubicar widgets en la nueva ventana
    labelName = ctk.CTkLabel(master=nueva_ventana, text="Nombre de la receta:", text_color="White", font=("Helvetica", 10))
    labelName.grid(row=0, column=0,pady=5, padx=5)

    entryName = ctk.CTkEntry(master=nueva_ventana, placeholder_text="Ingrese el nombre", corner_radius=10)
    entryName.grid(row=0, column=1,pady=5, padx=5)


    # Botón para confirmar la inserción
    buttonSubmit = ctk.CTkButton(master=nueva_ventana, text="Insertar", command=lambda: print("Receta insertada")) #lambda hace que el mensaje se muestre el el output
    buttonSubmit.pack(pady=20)

    # Función para manejar el cierre de la nueva ventana y mostrar la ventana principal nuevamente
    def on_close():
        nueva_ventana.destroy()  # Cierra la nueva ventana
        app.deiconify()  # Muestra la ventana principal nuevamente

    # Asignar la función on_close al evento de cerrar la ventana
    nueva_ventana.protocol("WM_DELETE_WINDOW", on_close)

# Crear el menú principal dentro del marco
menu = CTkMenuBar(master=app, padx=2)
menu.add_cascade("Insertar receta", command=insertarReceta)
menu.add_cascade("Buscar receta")
menu.add_cascade("Eliminar receta")

# Crear y ubicar los widgets en la ventana principal
labelName = ctk.CTkLabel(master=app, text="Name: ", text_color="white", font=("Helvetica", 14))
labelName.pack(pady=5, padx=5)

entryName = ctk.CTkEntry(app, placeholder_text="Enter your name", corner_radius=10)
entryName.pack(pady=5)

# Iniciar el bucle principal de la interfaz gráfica
app.mainloop()

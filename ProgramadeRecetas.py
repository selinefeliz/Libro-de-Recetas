# Importaciones
import tkinter
import customtkinter as ctk
from CTkMenuBar import *
import sqlite3
import bcrypt
from tkinter import messagebox
from PIL import Image, ImageTk  # Para manejar imágenes en los botones


# Configuración del modo de apariencia
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Crear la ventana principal
app = ctk.CTk()
app.geometry("560x580")
app.title("Recetas")

# Fuentes
font1 = ("Helvetica", 28, 'bold')
font2 = ("Georgia", 15, 'bold')
font3 = ("Arial", 13, 'bold')
font4 = ("Arial", 13, 'bold', 'underline')

# Variables globales para los frames
frame2 = None  # Frame de login
frame3 = None  # Frame del menú principal

# Conexión con sqlite
conexion = sqlite3.connect('data.db')
cursor = conexion.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
               username TEXT NOT NULL,
               password TEXT NOT NULL)''')

# Función para registrar un nuevo usuario
def signuUp():
    username = usuario_entry.get()
    password = password_entry.get()
    if username != '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Usuario ya existe.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username, hashed_password])
            conexion.commit()
            messagebox.showinfo('Info', 'Cuenta creada!')
    else:
        messagebox.showinfo('Error', 'Ingrese toda la información')

# Función para iniciar sesión
def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result:
            stored_hashed_password = result[0]
            if isinstance(stored_hashed_password, str):
                stored_hashed_password = stored_hashed_password.encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                messagebox.showinfo('Success', 'Logged in successfully.')
                frame_menu()  # Mostrar el menú principal
            else:
                messagebox.showerror('Error', 'Contraseña incorrecta')
        else:
            messagebox.showerror('Error', 'Usuario incorrecto')
    else:
        messagebox.showinfo('Error', 'Ingrese toda la información')

# Para mostrar el frame de login cuando se le de a ese botón
def logIn():
    global frame1  # Referencia a frame1 para destruirlo
    frame1.destroy()  # Destruir el frame de registro
    frame_login()

# Frame para iniciar sesión
def frame_login():
    global frame2  # Hacer el frame de login global para destruirlo más tarde
    frame2 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=660, height=580)
    frame2.place(x=0, y=0)

    image1 = ctk.CTkImage(light_image=Image.open("Imagenes/portada.jpg"), dark_image=Image.open("Imagenes/portada.jpg"), size=(270, 580))
    image1_lable = ctk.CTkLabel(frame2, image=image1, text="")
    image1_lable.place(x=0, y=0)
    frame2.image1 = image1

    login_label = ctk.CTkLabel(frame2, font=font1, text='Log in', text_color='#fff', bg_color='#001220')
    login_label.place(x=355, y=135)

    global username_entry2
    global password_entry2

    username_entry2 = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Usuario', placeholder_text_color='#a3a3a3', width=200, height=45)
    username_entry2.place(x=310, y=210)

    password_entry2 = ctk.CTkEntry(frame2, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Contraseña', placeholder_text_color='#a3a3a3', width=200, height=45)
    password_entry2.place(x=310, y=270)

    login_button2 = ctk.CTkButton(frame2, command=login_account, font=font2, text_color='#fff', text='Ingresar', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=140, height=40)
    login_button2.place(x=335, y=350)

# Función para volver al menú
def volverMenu():
    # Ocultar el frame de insertar receta
    frameInsertar.pack_forget()

    # Mostrar el frame del menú principal
    frame_menu()

# Variables globales para contar los pasos
paso_actual = 1
pasos_descripcion = {}
# Función para insertar receta
def insertarReceta():
    # Ocultar el frame del menú principal
    frame3.place_forget()

    # Crear el frame de insertar receta, ajustado al tamaño completo de la ventana
    global frameInsertar
    frameInsertar = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=660, height=580)
    frameInsertar.place(x=0, y=0)

    # Etiqueta para el título
    label = ctk.CTkLabel(frameInsertar, text="Insertar Nueva Receta", font=font1, text_color="#fff")
    label.grid(row=0, column=0, columnspan=2, pady=20)

    # Campo para el nombre de la receta
    labelNombre = ctk.CTkLabel(frameInsertar, font=font3, text="Nombre de la Receta:", text_color='#fff')
    labelNombre.grid(row=1, column=0, padx=30, pady=10, sticky="e")
    entryNombre = ctk.CTkEntry(frameInsertar, font=font3, width=250)
    entryNombre.grid(row=1, column=1, padx=40, pady=10, sticky="w")

    # Campo para la complejidad
    labelComplejidad = ctk.CTkLabel(frameInsertar, font=font3, text="Complejidad:", text_color='#fff')
    labelComplejidad.grid(row=2, column=0, padx=30, pady=10, sticky="e")
    complejidad = ctk.CTkComboBox(frameInsertar, values=["Baja", "Media", "Alta"], font=font3, width=250)
    complejidad.grid(row=2, column=1, padx=40, pady=10, sticky="w")

     # Campo para el tiempo total de preparación
    labelTiempo = ctk.CTkLabel(frameInsertar, font=font3, text="Tiempo Total (min):", text_color='#fff')
    labelTiempo.grid(row=3, column=0, padx=27, pady=10, sticky="e")
    entryTiempo = ctk.CTkEntry(frameInsertar, font=font3, width=250)
    entryTiempo.grid(row=3, column=1, padx=40, pady=10, sticky="w")
    
    # Etiqueta y entrada de paso actual (para ingresar paso por paso)
    global labelPaso, entryDetallesPasos
    labelPaso = ctk.CTkLabel(frameInsertar, font=font3, text=f"Paso {paso_actual}: Detalle", text_color='#fff')
    labelPaso.grid(row=4, column=0, padx=30, pady=10, sticky="e")
    entryDetallesPasos = ctk.CTkTextbox(frameInsertar, font=font3, width=250, height=210)
    entryDetallesPasos.grid(row=4, column=1, padx=40, pady=10, sticky="w")

    # Botón para agregar el paso actual
    buttonAgregarPaso = ctk.CTkButton(master=frameInsertar, text="Agregar Paso", font=font3, width=180, 
                                      fg_color="#2a9d8f", hover_color="#21867a", 
                                      command=lambda: agregarPaso(entryDetallesPasos))
    buttonAgregarPaso.grid(row=5, column=1, columnspan=2, pady=8)

    # Botón para finalizar la inserción de pasos y guardar la receta
    buttonFinalizar = ctk.CTkButton(master=frameInsertar, text="Finalizar Receta", font=font3,width=180,
                                    fg_color="#2a9d8f", hover_color="#001234")
    buttonFinalizar.grid(row=6, column=1, columnspan=2, pady=8)

    # Botón para regresar al menú principal
    buttonVolver = ctk.CTkButton(master=frameInsertar, text="Volver al menú", font=font3,width=180,
                                 fg_color="#121111", hover_color="#006e44", 
                                 command=volverMenu)
    buttonVolver.grid(row=7, column=1, columnspan=2, pady=10)

    # Ajustar la configuración de las columnas para centrar el formulario
    frameInsertar.grid_columnconfigure(0, weight=1)
    frameInsertar.grid_columnconfigure(1, weight=1)

# Función para agregar cada paso
def agregarPaso(entryDetallesPasos):
    global paso_actual, pasos_descripcion
    
    # Obtener el detalle del paso actual
    detalle = entryDetallesPasos.get("1.0", "end").strip()
    
    # Verificar que el detalle no esté vacío
    if detalle:
        pasos_descripcion[f"Paso {paso_actual}"] = detalle
        entryDetallesPasos.delete("1.0", "end")  # Limpiar el campo de texto para el siguiente paso
        paso_actual += 1  # Incrementar el contador de pasos

        # Actualizar el label para mostrar el siguiente paso
        labelPaso.configure(text=f"Paso {paso_actual}: Detalle")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese la descripción del paso actual.")



# Función para mostrar el menú principal
def frame_menu():
    global frame2, frame3  # Acceder a los frames globales
    if frame2:
        frame2.destroy()  # Destruir el frame de login si existe

    frame3 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=860, height=880)
    frame3.place(x=0, y=0)
    # Label 
    label = ctk.CTkLabel(frame3, font=font1, text='QUE DESEAS  HACER?', text_color='#fff')
    label.place(x=125, y=10)
    
    # Cargar iconos para los botones (ajusta las rutas a tus imágenes)
    insertar_icon = Image.open("Imagenes/Insertar.png")  # Ruta al icono de insertar
    insertar_icon = insertar_icon.resize((60, 60))  # Redimensionar el icono
    insertar_icon_tk = ImageTk.PhotoImage(insertar_icon)

    buscar_icon = Image.open("Imagenes/Buscar.png")  # Ruta al icono de buscar
    buscar_icon = buscar_icon.resize((60, 60))
    buscar_icon_tk = ImageTk.PhotoImage(buscar_icon)

    editar_icon = Image.open("Imagenes/Editar.png")  # Ruta al icono de editar
    editar_icon = editar_icon.resize((60, 60))
    editar_icon_tk = ImageTk.PhotoImage(editar_icon)

    eliminar_icon = Image.open("Imagenes/Eliminar.png")  # Ruta al icono de eliminar
    eliminar_icon = eliminar_icon.resize((60, 60))
    eliminar_icon_tk = ImageTk.PhotoImage(eliminar_icon)
    
    # Crear los botones como cuadros con iconos y distintos colores de fondo
    insertar_button = ctk.CTkButton(frame3, font=font2,text="Insertar receta", image=insertar_icon_tk, 
                                    compound="top", command=insertarReceta, width=210, height=170, 
                                    fg_color="#2a9d8f") 
    
    

    buscar_button = ctk.CTkButton(frame3,font=font2, text="Buscar receta", image=buscar_icon_tk, 
                                  compound="top", width=210, height=170, 
                                  fg_color="#264653")  # Color azul oscuro

    editar_button = ctk.CTkButton(frame3,font=font2, text="Editar receta", image=editar_icon_tk, 
                                  compound="top", width=210, height=170, 
                                  fg_color="#e9c46a")  # Color amarillo

    eliminar_button = ctk.CTkButton(frame3,font=font2, text="Eliminar receta", image=eliminar_icon_tk, 
                                    compound="top", width=210, height=170, 
                                    fg_color="#e76f51")  # Color rojo

    # # Posicionar los botones en una cuadrícula
    insertar_button.grid(row=0, column=0, padx=40, pady=60)
    buscar_button.grid(row=0, column=1, padx=40, pady=60)
    editar_button.grid(row=1, column=0, padx=40, pady=60)
    eliminar_button.grid(row=1, column=1, padx=40, pady=60)
    
    # Configurar el layout para centrar correctamente
    frame3.grid_columnconfigure((0, 1), weight=2)
    frame3.grid_rowconfigure((0, 1), weight=2)


# Frame inicial (Sign Up)
frame1 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=660, height=580)
frame1.place(x=0, y=0)

# Imagen de fondo
image1 = ctk.CTkImage(light_image=Image.open("Imagenes/portada.jpg"), dark_image=Image.open("Imagenes/portada.jpg"), size=(270, 580))
image1_lable = ctk.CTkLabel(frame1, image=image1, text="")
image1_lable.place(x=0, y=0)

# Label de Sign Up
signUp_label = ctk.CTkLabel(frame1, font=font1, text='Sign Up', text_color='#fff')
signUp_label.place(x=355, y=130)

# Entradas de usuario y contraseña
usuario_entry = ctk.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Usuario', placeholder_text_color='#a3a3a3', width=200, height=40)
usuario_entry.place(x=310, y=210)

password_entry = ctk.CTkEntry(frame1, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Contraseña', placeholder_text_color='#a3a3a3', width=200, height=45)
password_entry.place(x=310, y=270)

# Botón de Sign Up
signUp_button = ctk.CTkButton(frame1, command=signuUp, font=font2, text_color='#fff', text='Registrarse', fg_color='#006e44', hover_color='#3dcb4c', bg_color='#121111', cursor='hand2', corner_radius=5, width=140, height=40)
signUp_button.place(x=340, y=340)

# Label y botón de Login
login_label = ctk.CTkLabel(frame1, font=font3, text='Ya tienes una cuenta?', text_color='#fff')
login_label.place(x=330, y=390)

login_button = ctk.CTkButton(frame1, command=logIn, font=font4, text_color='White', text='Login', fg_color='#001a2e', hover_color='#00965d',corner_radius=5, cursor='hand2')
login_button.place(x=340, y=430)


# Loop principal
app.mainloop()

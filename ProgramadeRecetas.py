# Importaciones
import tkinter
import customtkinter as ctk
from CTkMenuBar import *
import sqlite3
import bcrypt
from tkinter import messagebox
from PIL import Image

# Configuración del modo de apariencia
ctk.set_appearance_mode("System")  # Establece el modo de color del sistema
ctk.set_default_color_theme("blue")  # Establece el tema de color predeterminado

# Crear la ventana principal
app = ctk.CTk()
app.geometry("450x360")
app.title("Recetas")

# Fuentes
font1 = ("Helvetica", 25, 'bold')
font2 = ("Arial", 17, 'bold')
font3 = ("Arial", 13, 'bold')
font4 = ("Arial", 13, 'bold', 'underline')

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
    frame1.destroy()  # Destruir el frame del login

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
                # Mostrar el menú principal
                mostrar_menu_principal()
            else:
                messagebox.showerror('Error', 'Contraseña incorrecta')
        else:
            messagebox.showerror('Error', 'Usuario incorrecto')
    else:
        messagebox.showinfo('Error', 'Ingrese toda la información')

# Para mostrar el frame de login cuando se le de a ese botón
def logIn():
    frame1.destroy()
    frame2 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=360)
    frame2.place(x=0, y=0)

    image1 = ctk.CTkImage(light_image=Image.open("Imagenes/portada.jpg"), dark_image=Image.open("Imagenes/portada.jpg"), size=(200, 360))
    image1_lable = ctk.CTkLabel(frame2, image=image1, text="")
    image1_lable.place(x=0, y=0)
    frame2.image1 = image1

    login_label = ctk.CTkLabel(frame2, font=font1, text='Log in', text_color='#fff', bg_color='#001220')
    login_label.place(x=280, y=20)

    global username_entry2
    global password_entry2

    username_entry2 = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Usuario', placeholder_text_color='#a3a3a3', width=200, height=45)
    username_entry2.place(x=230, y=80)

    password_entry2 = ctk.CTkEntry(frame2, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Contrasena', placeholder_text_color='#a3a3a3', width=200, height=45)
    password_entry2.place(x=230, y=150)

    login_button2 = ctk.CTkButton(frame2, command=login_account, font=font2, text_color='#fff', text='Ingresar', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
    login_button2.place(x=270, y=220)

# Función para insertar receta
def insertarReceta():
    
    nueva_ventana = ctk.CTkToplevel(app)
    nueva_ventana.geometry("600x540")
    nueva_ventana.title("Insertar receta")

    labelName = ctk.CTkLabel(master=nueva_ventana, text="Nombre de la receta:", text_color="White", font=("Helvetica", 10))
    labelName.grid(row=0, column=0, pady=5, padx=5)

    entryName = ctk.CTkEntry(master=nueva_ventana, placeholder_text="Ingrese el nombre", corner_radius=10)
    entryName.grid(row=0, column=1, pady=5, padx=5)

    buttonSubmit = ctk.CTkButton(master=nueva_ventana, text="Insertar", command=lambda: print("Receta insertada"))
    buttonSubmit.pack(pady=20)

    # def on_close():
    #     nueva_ventana.destroy()
    #     app.deiconify()

    # nueva_ventana.protocol("WM_DELETE_WINDOW", on_close)

def mostrar_menu_principal():
    frame_menu = ctk.CTkToplevel(app)
    frame_menu.geometry("600x540")
    frame_menu.title('Menu Principal')
    
    # Crear el menú principal
    menu = CTkMenuBar(frame_menu, padx=2)
    
    # Añadir las opciones del menú
    menu.add_cascade("Insertar receta", command=insertarReceta, text_color="white")
    menu.add_cascade("Buscar receta", text_color="white")
    menu.add_cascade("Eliminar receta", text_color="white")

    # Empaquetar el menú
    menu.pack(y=0)


# Frame inicial (Sign Up)
frame1 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=360)
frame1.place(x=0, y=0)

# Imagen de fondo
image1 = ctk.CTkImage(light_image=Image.open("Imagenes/portada.jpg"), dark_image=Image.open("Imagenes/portada.jpg"), size=(200, 360))
image1_lable = ctk.CTkLabel(frame1, image=image1, text="")
image1_lable.place(x=0, y=0)

# Label de Sign Up
signUp_label = ctk.CTkLabel(frame1, font=font1, text='Sign Up', text_color='#fff', bg_color='#001220')
signUp_label.place(x=280, y=20)

# Entradas de usuario y contraseña
usuario_entry = ctk.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Usuario', placeholder_text_color='#a3a3a3', width=200, height=45)
usuario_entry.place(x=230, y=80)

password_entry = ctk.CTkEntry(frame1, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Contrasena', placeholder_text_color='#a3a3a3', width=200, height=45)
password_entry.place(x=230, y=150)

# Botón de Sign Up
signUp_button = ctk.CTkButton(frame1, command=signuUp, font=font2, text_color='#fff', text='Registrarse', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
signUp_button.place(x=270, y=220)

# Label y botón de Login
login_label = ctk.CTkLabel(frame1, font=font3, text='Ya tienes una cuenta?', text_color='#fff', bg_color='#001220')
login_label.place(x=230, y=250)

login_button = ctk.CTkButton(frame1, command=logIn, font=font4, text_color='#00bf77', text='Login', fg_color='#001220', hover_color='#001220', cursor='hand2', width=35, height=20)
login_button.place(x=380, y=250)

# Iniciar el loop de la aplicación
app.mainloop()

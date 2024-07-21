import tkinter as tk
from tkinter import ttk,Tk, messagebox
from PIL import Image, ImageTk
import pymysql
from tkinter import Button
from tkinter import messagebox
from Llamada import admin_menu

def boton_regreso(frame_2, frame):
    boton_volver1 = Button(frame_2, text="Volver", bg="grey", command=lambda: mostrar_frame(frame), font=("Times New Roman", 14))
    boton_volver1.place(x=10, y=675)

def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("1200x720")  # Tamaño de la ventana
    pantalla.config(bg="black")


    global frame_principal
    frame_principal = tk.Frame(pantalla, bg="grey")
    frame_principal.place(x=0, y=0, width=1200, height=720)

    
    etiqueta1 = tk.Label(frame_principal,text="Acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()

    boton1 = Button(frame_principal,text="Iniciar sesión", height="3", width="30", command=inicio_sesion).pack()
   

    boton2 = Button(frame_principal,text="Registrar", height="3", width="30", command=registrar).pack()

    pantalla.mainloop()



def inicio_sesion():
    global pantalla1
    pantalla1 = tk.Frame(pantalla, bg="black")
    pantalla1.place(x=0, y=0, width=1200, height=720)
    
    boton_regreso(pantalla1, main_frame)

    tk.Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña\n a continuación", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    tk.Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=tk.StringVar()
    contrasenausuario_verify=tk.StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    tk.Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry=tk.Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()

    tk.Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry=tk.Entry(pantalla1,show="*" ,textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    tk.Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión", command=validacion_datos).pack()
    
    
    
   
def registrar():
    global pantalla2
    pantalla2 = tk.Frame(pantalla, bg="black")
    pantalla2.place(x=0, y=0, width=1200, height=720)

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=tk.StringVar()
    contrasena_entry=tk.StringVar()

    tk.Label(pantalla2, text="Por favor ingrese un Usuario y Contraseña\n de su elección, para el registro del Sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    tk.Label(pantalla2, text="").pack()

    tk.Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry=tk.Entry(pantalla2)
    nombreusuario_entry.pack()
    tk.Label(pantalla2).pack()

    tk.Label(pantalla2, text="Contraseña").pack()
    contrasena_entry=tk.Entry(pantalla2, show="*")
    contrasena_entry.pack()
    tk.Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=inserta_datos).pack()

    boton_regreso(pantalla2, frame_principal)
    

def inserta_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    fcursor=bd.cursor()

    sql="INSERT INTO login (usuario, contrasena) VALUES ('{0}','{1}')".format(nombreusuario_entry.get(), contrasena_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        tk.messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        tk.messagebox.showinfo(message="No registrado", title="Aviso")

    bd.close()

def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    with bd.cursor() as cursor:
        # Ejecutar una consulta
        a = "SELECT id, usuario, contrasena FROM login"
        cursor.execute(a)

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]

        # Obtener los resultados
        results = cursor.fetchall()

        # Procesar los resultados
        for row in results:
            data = dict(zip(column_names, row))

            id = data['id']
            pelicula = data['usuario']
            imagen = data['contrasena']

            # Hacer algo con los valores
            print(f"ID: {id}, Pelicula: {pelicula}, Ruta imagen: {imagen}")

    fcursor=bd.cursor()

    fcursor.execute("SELECT contrasena from login WHERE usuario='"+nombre_usuario_entry.get()+"' and contrasena='"+contrasena_usuario_entry.get()+"'")

    if fcursor.fetchall():
        tk.messagebox.showinfo(title="Inicio de Sesión correcto", message="Usuario y Contraseña correcta")
        root.destroy()
        pantalla.destroy()
        admin_menu()
    else:
        tk.messagebox.showinfo(title="Inicio de Sesión incorrecto", message="Usuario y Contraseña incorrecta")
        
    
    bd.close()

def mostrar_frame(frame):
    frame.tkraise()


def abrir_nueva_ventana(titulo, image_path, frame_funciones, hor1,hor2,hor3):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title(titulo)
    nueva_ventana.geometry("1200x720")
    
    # Añadir contenido específico en cada nueva ventana
    label = tk.Label(nueva_ventana, text=f"Contenido de {titulo}")
    label.pack(padx=20, pady=20)
    
    # Mostrar la imagen también en la nueva ventana
    try:
        image = Image.open(image_path)
        image = image.resize((400, 500))
        photo = ImageTk.PhotoImage(image)

        label_image = tk.Label(nueva_ventana, image=photo)
        label_image.image = photo  # Mantener una referencia a la imagen
        label_image.pack(padx=5, pady=5)
    except Exception as e:
        print(f"Error al cargar la imagen {image_path}: {e}")
        label_error = tk.Label(nueva_ventana, text=f"Error al cargar la imagen {image_path}", fg="red")
        label_error.pack(padx=5, pady=5)
    
    # Añadir un botón con una acción específica para esta ventana
    def accion_especifica():
        tk.Label(nueva_ventana, text="¡Acción realizada!").pack(padx=20, pady=20)
    
    boton_accion = tk.Button(nueva_ventana, text="Realizar Acción", command=accion_especifica)
    boton_accion.pack(padx=10, pady=10)
    
    # Crear botones con la función bot
    
    
    
    def etiquetas_hora_funciones(frame, titulo, tex1, tex2, tex3):
        global contador
        global valor_guardado
        global confirmacion_confirmada

        def contar_clics():
            global contador
            if contador == 25:
                messagebox.showinfo(message="Límite de asientos alcanzado", title="Aviso")
            else:
                contador += 1
                label_contador.config(text=contador)

        def restar():
            global contador
            if contador > 0:
                contador -= 1
                label_contador.config(text=contador)

        def confirmar():
            global valor_guardado
            global confirmacion_confirmada
            valor_guardado = contador 
            if valor_guardado == 0:
                messagebox.showinfo(message="Elija entradas", title="Aviso")
            else:
                label_confirmacion.config(text=f"Entradas: {valor_guardado}")
                confirmacion_confirmada = True
                # Actualizar los botones después de confirmar
                bot(nueva_ventana, frame_funciones)
                print(valor_guardado)

        # Inicializar el contador y valor final
        contador = 0
        confirmacion_confirmada = False

        # Función para crear botones en los frames de sala
        def bot(frame, frame_funciones):
            for h in range(3):
                # Capturar el valor de h en el closure
                frame_funcion = frame_funciones[h]
                estado = "normal" if confirmacion_confirmada else "disabled"
                boton = Button(frame, text=f"Sala {h+1}", command=lambda f=frame_funcion: mostrar_frame(f), bg="black", fg="white", font=("Times New Roman", 25), state=estado)
                boton.place(x=300, y=50 + 200 * h, width=200, height=100)

        # Crear elementos de la interfaz
        etiqueta = tk.Label(nueva_ventana, text=titulo, bg="black", fg="white", font=("Times New Roman", 25))
        etiqueta.place(x=910, y=560)

        e_sala1 = tk.Label(nueva_ventana, text=tex1, bg="black", fg="white", font=("Times New Roman", 25))
        e_sala1.place(x=30, y=90)

        e_sala2 = tk.Label(nueva_ventana, text=tex2, bg="black", fg="white", font=("Times New Roman", 25))
        e_sala2.place(x=30, y=280)

        e_sala3 = tk.Label(nueva_ventana, text=tex3, bg="black", fg="white", font=("Times New Roman", 25))
        e_sala3.place(x=30, y=480)

        e_entradas = tk.Label(nueva_ventana, text="2D General ", bg="black", fg="white", font=("Times New Roman", 25))
        e_entradas.place(x=30, y=600)

        label_contador = tk.Label(nueva_ventana, text="0", bg="black", fg="white", font=("Times New Roman", 18))
        label_contador.place(x=348, y=599)

        boton_suma = Button(nueva_ventana, text="+", bg="blue", fg="white", font=("Times New Roman", 20), command=contar_clics)
        boton_suma.place(x=390, y=590)

        boton_resta = Button(nueva_ventana, text="-", bg="blue", fg="white", font=("Times New Roman", 20), command=restar)
        boton_resta.place(x=300, y=590)

        boton_confirmar = Button(nueva_ventana, text="Confirmar", font=("Times New Roman", 20), fg="white", bg="blue", command=confirmar)
        boton_confirmar.place(x=600, y=590)

        label_confirmacion = tk.Label(nueva_ventana, text="Entradas: Ninguna",font=("Times New Roman", 20), fg="white", bg="black")
        label_confirmacion.place(x=400, y=670)

        valor_guardado = contador
        print(valor_guardado)
        
            
    
    etiquetas_hora_funciones(nueva_ventana, f"{titulo}", f"{hor1}", f"{hor2}", f"{hor3}")

    

def load_data():
    con = 0
    A = 0
    M = 0
    # Conectar a la base de datos MySQL
    connection = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )
    cursor = connection.cursor()
    
    # Obtener los datos
    cursor.execute('SELECT pelicula, imagen, Horario1, Horario2, Horario3 FROM prueba')
    data = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
    connection.close()

    # Mostrar los datos en el frame
    for i, (title, image_path, hor1, hor2, hor3) in enumerate(data):
        # Mostrar el título
        label_title = tk.Label(inner_frame, text=title, font=("Helvetica", 16))
        label_title.grid(row=1 + M, column=i - A, padx=5, pady=10)
        con += 1

        # Cargar y mostrar la imagen
        try:
            image = Image.open(image_path)
            image = image.resize((400, 500))
            photo = ImageTk.PhotoImage(image)

            label_image = tk.Label(inner_frame, image=photo)
            label_image.image = photo  # Mantener una referencia a la imagen
            label_image.grid(row=2 + M, column=i - A, padx=5, pady=10)
        except Exception as e:
            print(f"Error al cargar la imagen {image_path}: {e}")
            label_error = tk.Label(inner_frame, text=f"Error al cargar la imagen {image_path}", fg="red")
            label_error.grid(row=2 + M, column=i - A, padx=5, pady=10)

        # Crear frames y funciones para los botones
        frame_funciones = [tk.Frame(root, bg="gray", width=00, height=00) for _ in range(3)]
        for f in frame_funciones:
            f.place(x=0, y=0, width=00, height=00)

        # Botón para abrir una nueva ventana
        boton_nueva_ventana = tk.Button(inner_frame, text="Abrir Nueva Ventana", 
                                        command=lambda t=title, p=image_path, f=frame_funciones, h1=hor1,h2=hor2,h3=hor3: abrir_nueva_ventana(t, p, f,h1,h2,h3))
        boton_nueva_ventana.grid(row=3 + A, column=i - A, padx=5, pady=10)
        if con % 3 == 0:
            A += 3
            M += 3

# Crear la ventana principal
root = tk.Tk()
root.title("Cargar Datos desde Base de Datos")
root.geometry("800x600")

# Crear un frame para contener el canvas y la scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# Crear un canvas
canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Añadir una scrollbar al canvas
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar el canvas para usar la scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Crear un frame dentro del canvas
inner_frame = tk.Frame(canvas)

# Añadir el frame al canvas
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Botón para cargar los datos
load_data()
#Boton para ingresar al usuario administrador
bot_log=Button(main_frame, text="Iniciar sesión", command=lambda: menu_pantalla(), fg="white", bg="blue", font=("Times New Roman", 27))
bot_log.place(x=1100, y=10, height=70)

# Ejecutar el bucle principal de Tkinter
root.mainloop()



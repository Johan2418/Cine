import tkinter as tk
from tkinter import ttk, Tk, messagebox
from PIL import Image, ImageTk
import pymysql
from tkinter import Button
from tkinter import messagebox
from Llamada import admin_menu
import os
import json

def boton_regreso(frame_2, frame):
    boton_volver1 = Button(frame_2, text="Volver", bg="grey", command=lambda: mostrar_frame(frame), font=("Times New Roman", 14))
    boton_volver1.place(x=10, y=675)

def mostrar_frame(frame):
    frame.tkraise()


def crear_frames(root, n, ):
    frames = []
    for i in range(n):
        frame_name = f"frame_{i+1}"
        frame = tk.Frame(root, bg="black", name=frame_name)  # Añadir name para identificación
        frame.place(x=0, y=0, width=1200, height=720)
        frames.append(frame)
    return frames


def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("1200x720")  # Tamaño de la ventana
    pantalla.config(bg="black")

    global frame_principal
    frame_principal = tk.Frame(pantalla, bg="grey")
    frame_principal.place(x=0, y=0, width=1200, height=720)

    etiqueta1 = tk.Label(frame_principal, text="Acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()

    boton1 = Button(frame_principal, text="Iniciar sesión", height="3", width="30", command=inicio_sesion).pack()
    boton2 = Button(frame_principal, text="Registrar", height="3", width="30", command=registrar).pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1 = tk.Frame(pantalla, bg="black")
    pantalla1.place(x=0, y=0, width=1200, height=720)

    boton_regreso(pantalla1, frame_principal)

    tk.Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña\n a continuación", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    tk.Label(pantalla1, text="", bg=("black")).pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify = tk.StringVar()
    contrasenausuario_verify = tk.StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    tk.Label(pantalla1, text="Usuario", font=("Calibri", 15)).pack()
    nombre_usuario_entry = tk.Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()

    tk.Label(pantalla1, text="Contraseña", font=("Calibri", 15)).pack()
    contrasena_usuario_entry = tk.Entry(pantalla1, show="*", textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    tk.Label(pantalla1, bg=("black")).pack()

    Button(pantalla1, text="Iniciar Sesión", font=("Calibri", 15), command=validacion_datos).pack()

def registrar():
    global pantalla2
    pantalla2 = tk.Frame(pantalla, bg="black")
    pantalla2.place(x=0, y=0, width=1200, height=720)

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry = tk.StringVar()
    contrasena_entry = tk.StringVar()

    tk.Label(pantalla2, text="Por favor ingrese un Usuario y Contraseña\n de su elección, para el registro del Sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    tk.Label(pantalla2, text="", bg=("black")).pack()

    tk.Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry = tk.Entry(pantalla2)
    nombreusuario_entry.pack()
    tk.Label(pantalla2, bg=("black")).pack()

    tk.Label(pantalla2, text="Contraseña").pack()
    contrasena_entry = tk.Entry(pantalla2, show="*")
    contrasena_entry.pack()
    tk.Label(pantalla2, bg=("black")).pack()

    Button(pantalla2, text="Registrar", command=inserta_datos).pack()

    boton_regreso(pantalla2, frame_principal)

def inserta_datos():
    bd = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    fcursor = bd.cursor()

    sql = "INSERT INTO login (usuario, contrasena) VALUES ('{0}','{1}')".format(nombreusuario_entry.get(), contrasena_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        tk.messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        tk.messagebox.showinfo(message="No registrado", title="Aviso")

    bd.close()

def validacion_datos():
    bd = pymysql.connect(
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

    fcursor = bd.cursor()

    fcursor.execute("SELECT contrasena from login WHERE usuario='" + nombre_usuario_entry.get() + "' and contrasena='" + contrasena_usuario_entry.get() + "'")

    if fcursor.fetchall():
        tk.messagebox.showinfo(title="Inicio de Sesión correcto", message="Usuario y Contraseña correcta")
        root.destroy()
        pantalla.destroy()
        admin_menu()
    else:
        tk.messagebox.showinfo(title="Inicio de Sesión incorrecto", message="Usuario y Contraseña incorrecta")

    bd.close()

def abrir_nueva_ventana(titulo, image_path, frame_funciones, hor1, hor2, hor3, sala):
    print(sala)

    x = tk.Toplevel(root)
    x.title(titulo)
    x.geometry("1200x720")
    x.config(bg="black")
    nueva_ventana = tk.Frame(x, bg="black")  # Añadir name para identificación
    nueva_ventana.place(x=0, y=0, width=1200, height=720)

    # Añadir contenido específico en cada nueva ventana
    label = tk.Label(nueva_ventana, text=f"Contenido de {titulo}", bg="black", fg="white", font=("Helvetica", 18))
    label.pack(padx=20, pady=10)

    # Mostrar la imagen también en la nueva ventana
    try:
        image_path = image_path.strip()
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"La ruta {image_path} no existe o no es un archivo.")
        if not os.access(image_path, os.R_OK):
            raise PermissionError(f"No tienes permiso para leer el archivo {image_path}.")
        image = Image.open(image_path)
        image = image.resize((400, 500))
        photo = ImageTk.PhotoImage(image)
        label_image = tk.Label(nueva_ventana, image=photo)
        label_image.image = photo  # Mantener una referencia a la imagen
        label_image.place(x=680, y=50)
    except Exception as e:
        print(f"Error al cargar la imagen {image_path}: {e}")
        label_error = tk.Label(nueva_ventana, text=f"Error al cargar la imagen {image_path}", fg="red")
        label_error.pack(padx=5, pady=5)

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
                bot(nueva_ventana, frame_funciones)
                print(valor_guardado)

        contador = 0
        confirmacion_confirmada = False

        def create_new_window(sala, t):#ahcer 3 frames
            new_frame = tk.Frame(x, bg="black")# hacer una condicion que si es sala1 sea en frame[0]
            new_frame.place(x=0, y=0, width=1200, height=720)
            if t == "Sala 1":
                
                matriz_botones = crear_matriz(new_frame, sala)  # Pasar el número de sala como parámetro y obtener la matriz creada
                matriz_botones_por_sala[sala] = matriz_botones  # Guardar la matriz creada en un diccionario
                back_button = tk.Button(new_frame, text="Volver", bg="blue", fg="white", font=("Times New Roman", 15), command=lambda: mostrar_frame(nueva_ventana))
                back_button.place(x=0, y=665)
                mostrar_mejores(new_frame, matriz_botones)
                mostrar_frame(new_frame)
            if t == "Sala 2":
                sala = 2
                matriz_botones = crear_matriz(new_frame, sala)  # Pasar el número de sala como parámetro y obtener la matriz creada
                matriz_botones_por_sala[sala] = matriz_botones  # Guardar la matriz creada en un diccionario
                back_button = tk.Button(new_frame, text="Volver", bg="blue", fg="white", font=("Times New Roman", 15), command=lambda: mostrar_frame(nueva_ventana))
                back_button.place(x=0, y=665)
                mostrar_mejores(new_frame, matriz_botones)
                mostrar_frame(new_frame)
            if t == "Sala 3":
                sala = 3     
                matriz_botones = crear_matriz(new_frame, sala)  # Pasar el número de sala como parámetro y obtener la matriz creada
                matriz_botones_por_sala[sala] = matriz_botones  # Guardar la matriz creada en un diccionario
                back_button = tk.Button(new_frame, text="Volver", bg="blue", fg="white", font=("Times New Roman", 15), command=lambda: mostrar_frame(nueva_ventana))
                back_button.place(x=0, y=665)
                mostrar_mejores(new_frame, matriz_botones)
                mostrar_frame(new_frame)

        def bot(frame, frame_funciones):
            for h in range(3):
                frame_funcion = frame_funciones[h]
                estado = "normal" if confirmacion_confirmada else "disabled"
                textoxd = f"Sala {h+1}"
                boton = Button(frame, text=textoxd, command=lambda s=sala, t = textoxd: create_new_window(s, t), bg="blue", fg="white", font=("Times New Roman", 25), state=estado)
                boton.place(x=300, y=50 + 200 * h, width=200, height=100)

        etiqueta = tk.Label(nueva_ventana, text=titulo, bg="black", fg="white", font=("Times New Roman", 25))
        etiqueta.place(x=700, y=560)
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
        boton_confirmar.place(x=510, y=590)

        label_confirmacion = tk.Label(nueva_ventana, text="Entradas: Ninguna", font=("Times New Roman", 20), fg="white", bg="black")
        label_confirmacion.place(x=400, y=670)

        valor_guardado = contador


    etiquetas_hora_funciones(nueva_ventana, f"{titulo}", f"{hor1}", f"{hor2}", f"{hor3}")
    mostrar_frame(nueva_ventana)


def load_data():
    con = 0
    A = 0
    M = 0
    sala_counter = 1  # Inicializa un contador de sala

    connection = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )
    cursor = connection.cursor()

    cursor.execute('SELECT pelicula, imagen, Horario1, Horario2, Horario3 FROM prueba')
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    for i, (title, image_path, hor1, hor2, hor3) in enumerate(data):
        label_title = tk.Label(inner_frame, fg="white", bg="black", text=title, font=("Helvetica", 18))
        label_title.grid(row=1 + M, column=i - A, padx=5, pady=10)
        con += 1

        try:
            image = Image.open(image_path)
            image = image.resize((400, 500))
            photo = ImageTk.PhotoImage(image)

            label_image = tk.Label(inner_frame, image=photo)
            label_image.image = photo
            label_image.grid(row=2 + M, column=i - A, padx=5, pady=10)
        except Exception as e:
            print(f"Error al cargar la imagen {image_path}: {e}")
            label_error = tk.Label(inner_frame, text=f"Error al cargar la imagen {image_path}", fg="red")
            label_error.grid(row=2 + M, column=i - A, padx=5, pady=10)

        frame_funciones = [tk.Frame(root, bg="gray", width=0, height=0) for _ in range(10)]
        for f in frame_funciones:
            f.place(x=0, y=0, width=0, height=0)

        boton_nueva_ventana = tk.Button(inner_frame, text="Ingresar", font=("Times New Roman", 18), fg="white", bg="blue",
                                        command=lambda t=title, p=image_path, f=frame_funciones, h1=hor1, h2=hor2, h3=hor3, s=sala_counter: abrir_nueva_ventana(t, p, f, h1, h2, h3, s))
        boton_nueva_ventana.grid(row=3 + A, column=i - A, padx=5, pady=10)

        sala_counter += 1  # Incrementa el contador de sala

        if con % 3 == 0:
            A += 3
            M += 3


matriz_botones_por_sala = {} 
def guardar_estado_botones(matriz_botones, sala):
    estado_botones = [[boton["bg"] for boton in fila] for fila in matriz_botones]
    with open(f'estado_sala_{sala}.json', 'w') as archivo:
        json.dump(estado_botones, archivo)

def cargar_estado_botones(sala):
    try:
        with open(f'estado_sala_{sala}.json', 'r') as archivo:
            estado_botones = json.load(archivo)
        return estado_botones
    except FileNotFoundError:
        return None


def crear_matriz(frame, sala):
    def verificar_rojo():
        for fila in matriz_botones:
            for boton in fila:
                if boton["bg"] == "blue":
                    boton.config(bg="red", text="O")
        guardar_estado_botones(matriz_botones, sala)  # Guardar el estado de los botones
                
    def verificar():
        for fila in matriz_botones:
            for boton in fila:
                if boton["bg"] == "yellow":
                    boton.config(bg="red", text="O")
        guardar_estado_botones(matriz_botones, sala)  # Guardar el estado de los botones

    def cambiar_color(boton):
        nonlocal seleccionados
        if seleccionados < valor_guardado:
            if boton["bg"] == "green":
                boton.config(bg="blue", text="R")
                seleccionados += 1
            elif boton["bg"] == "blue":
                boton.config(bg="green", text="L")
                seleccionados -= 1
            elif boton["bg"] == "yellow":
                boton.config(bg="blue", text="R")
        else:
            if boton["bg"] == "blue":
                boton.config(bg="green", text="L")
                seleccionados -= 1

    matriz_botones = []
    seleccionados = 0

    n_fila = 0 
    nasci = 64
    letras_filas = []
    numeros_filas = []

    for i in range(5):
        nasci += 1
        nasci = chr(nasci)
        fila_frame = tk.Frame(frame, bg="black")
        fila_frame.pack()
        fila_botones = []

        n_fila += 1
        numeros_filas.append(n_fila)
        letras_filas.append(nasci)
        letras_filas.sort(reverse=True)

        for idx, letra in enumerate(letras_filas):
            etiq_1 = tk.Label(frame, text=letra, font=("Arial", 20), fg="white", bg="black")
            etiq_1.place(x=40, y=55 + idx * 60)
        nasci = ord(nasci)

        for id, nf in enumerate(numeros_filas):
            etiq_2 = tk.Label(frame, text=nf, font=("Arial", 20), fg="white", bg="black")
            etiq_2.place(x=100 + id * 90, y=10)

        for j in range(5):
            boton = Button(frame, text="L", bg="green", font=("Times New Roman", 25))
            boton.config(command=lambda b=boton: cambiar_color(b))
            boton.place(x=(j + 0.80) * 90, y=(i + 0.80) * 60, width=90, height=55)
            fila_botones.append(boton)

        matriz_botones.append(fila_botones)

    estado_botones = cargar_estado_botones(sala)
    if estado_botones:
        for i, fila in enumerate(estado_botones):
            for j, color in enumerate(fila):
                matriz_botones[i][j].config(bg=color, text="O" if color == "red" else "R" if color == "blue" else "L")

    boton_volver1 = Button(frame, text="Reservar", bg="black", fg="white", font=("Times New Roman", 25), command=verificar_rojo)
    boton_volver1.place(x=795, y=290)

    botonr = Button(frame, text="Reservar Mejores \nAsientos ", fg="white", bg="black", font=("Times New Roman", 25), command=verificar)
    botonr.place(x=740, y=150)

    botoncol = tk.Label(frame, bg="green", font=("Times New Roman", 15), fg="white", text="     ")
    botoncol.place(x=750, y=500)

    botmen = tk.Label(frame, bg="black", font=("Times New Roman", 15), fg="white", text="Libre")
    botmen.place(x=815, y=500)

    botoncol = tk.Label(frame, bg="red", font=("Times New Roman", 15), fg="white", text="     ")
    botoncol.place(x=750, y=550)

    botmen1 = tk.Label(frame, bg="black", font=("Times New Roman", 15), fg="white", text="Ocupado")
    botmen1.place(x=815, y=550)

    botoncol = tk.Label(frame, bg="blue", font=("Times New Roman", 15), fg="white", text="     ")
    botoncol.place(x=750, y=600)

    botmen2 = tk.Label(frame, bg="black", font=("Times New Roman", 15), fg="white", text="Reservado")
    botmen2.place(x=815, y=600)

    return matriz_botones  # Devolver la matriz de botones


# Inicializa una variable global para rastrear si ya se han mostrado los mejores asientos
# Inicializa una variable global para rastrear si ya se han mostrado los mejores asientos
mejores_asientos_mostrados = False
valor_guardado = 0  # Inicializa el valor guardado

def confirmar_valor(nuevo_valor):
    global valor_guardado, mejores_asientos_mostrados
    valor_guardado = nuevo_valor
    mejores_asientos_mostrados = False  # Reinicia la bandera cuando se confirma un nuevo valor

def actualizar_mejores_asientos(matriz_botones):
    global mejores_asientos_mostrados
    
    # Verifica si ya se han mostrado los mejores asientos
    if mejores_asientos_mostrados:
        return []

    mejores_asientos = []
    
    def es_disponible(f, c):
        return matriz_botones[f][c]["bg"] == "green"
    
    def marcar_mejor_asiento(fila, columna):
        matriz_botones[fila][columna].config(bg="yellow", text="M")
        mejores_asientos.append((fila, columna))

    cantidad = valor_guardado  # Usar la cantidad confirmada para seleccionar los mejores asientos
    
    for J in range(4, -1, -1):
        if cantidad == 0:
            break
        
        if es_disponible(J, 2) and cantidad >= 1:
            marcar_mejor_asiento(J, 2)
            cantidad -= 1
        if es_disponible(J, 3) and es_disponible(J, 1) and cantidad >= 2:
            marcar_mejor_asiento(J, 3)
            marcar_mejor_asiento(J, 1)
            cantidad -= 2
        if es_disponible(J, 3) and cantidad >= 1:
            marcar_mejor_asiento(J, 3)
            cantidad -= 1
        if es_disponible(J, 1) and cantidad >= 1:
            marcar_mejor_asiento(J, 1)
            cantidad -= 1
        if es_disponible(J, 4) and es_disponible(J, 0) and cantidad >= 2:
            marcar_mejor_asiento(J, 4)
            marcar_mejor_asiento(J, 0)
            cantidad -= 2
        if es_disponible(J, 4) and cantidad >= 1:
            marcar_mejor_asiento(J, 4)
            cantidad -= 1
        if es_disponible(J, 0) and cantidad >= 1:
            marcar_mejor_asiento(J, 0)
            cantidad -= 1

    # Marca la bandera como verdadero para indicar que ya se mostraron los mejores asientos
    mejores_asientos_mostrados = True

    return mejores_asientos



def mostrar_mejores(frame,boton):
    
    def mostrar_mejores_asientos():
        

        mejores_asientos = actualizar_mejores_asientos(boton) 
        
        # Ejemplo: usando la matriz de la primera función del primer frame
    # Suponiendo que tienes una etiqueta para mostrar los mejores asientos en tu interfaz gráfico
        if mejores_asientos:
            mensaje = "Los mejores asientos son:\n"
        else:
            label_mejores_asientos.config(text="No hay mejores asientos disponibles.")
            
    label_mejores_asientos = tk.Label(frame, text="",fg="white", bg="black", font=("Times New Roman", 28))
    label_mejores_asientos.place(x=50, y=540)

    # Suponiendo que tienes un botón en tu interfaz que al presionarlo se llama mostrar_mejores_asientos
    boton_mostrar_mejores = Button(frame, text="Mostrar Mejores \nAsientos",font=("Times New Roman", 25),fg="white", bg="black", command=mostrar_mejores_asientos)
    boton_mostrar_mejores.place(x=740, y=10)
    confirmar_valor(valor_guardado)




# Crear la ventana principal
root = tk.Tk()
root.title("Cine")
root.geometry("1920x1080")
root.config(bg="black")

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
bot_log=Button(main_frame, text="Iniciar sesión", command=lambda: menu_pantalla(), fg="white", bg="blue", font=("Times New Roman", 20))
bot_log.place(x=1300, y=10, height=70)

# Ejecutar el bucle principal de Tkinter
root.mainloop()
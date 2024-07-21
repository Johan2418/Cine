import tkinter as tk
from tkinter import ttk,Tk, messagebox
from PIL import Image, ImageTk
import pymysql
from tkinter import Button
from tkinter import messagebox
from Modo_Andmin import admin_pantalla

def admin_menu():
    def mostrar_frame(frame):
        frame.tkraise()


    def abrir_nueva_ventana(titulo, image_path, frame_funciones):
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
            
                
        
        etiquetas_hora_funciones(nueva_ventana, "Spiderman \nNo Way \nHome", "Funcion 13:00", "Funcion 14:00", "Funcion 13:00")

        
        
        
        
        
        
        
        

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
        cursor.execute('SELECT pelicula, imagen FROM prueba')
        data = cursor.fetchall()

        # Cerrar la conexión
        cursor.close()
        connection.close()

        # Mostrar los datos en el frame
        for i, (title, image_path) in enumerate(data):
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
                                            command=lambda t=title, p=image_path, f=frame_funciones: abrir_nueva_ventana(t, p, f))
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
    bot_log=Button(main_frame, text="Editar", command=lambda: admin_pantalla(), fg="white", bg="blue", font=("Times New Roman", 27))
    bot_log.place(x=1100, y=10, height=70)

    # Ejecutar el bucle principal de Tkinter
    root.mainloop()

from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from tkinter import filedialog, Tk
import pymysql 
from Datos import row, results, id, column_names
import os
import shutil


IDD=id+1


def admin_pantalla():
    global root1
    # Crear variable para abrir ventana y nombre
    root1 = Tk()
    root1.title("Cine")  # Nombre
    root1.geometry("1200x720")  # Tamaño de la ventana
    root1.config(bg="black")  # Color de la ventana
    

    global frame_crear_peli, frame_pelis, frames_modi
    frame_crear_peli = crear_frames(root1, 1, "peli")[0]
    frame_pelis = crear_frames(root1, 1, "pelicyula")[0]
    frames_modi = crear_frames(root1, 3, "modificador")

    boton_regreso(frames_modi[0], frame_crear_peli)
    boton_regreso(frames_modi[2], frame_crear_peli)
    #Valores para los combobox

    # Crear las etiquetas y entradas de texto fuera de la función ingresar_nombre
    global L, entrada_nombre,boton_confirmar,L2,entrada_hor1,L3,entrada_hor2, L4, entrada_hor3
    L = Label(frames_modi[0], text="Nombre de Pelicula", fg="white", bg="black", font=("Times New Roman", 18))
    entrada_nombre = Entry(frames_modi[0], font=("Times New Roman", 20))
    L2 = Label(frames_modi[0], text="Horario 1", fg="white", bg="black", font=("Times New Roman", 18))
    entrada_hor1 = ttk.Combobox(frames_modi[0], font=("Times New Roman", 20))
    entrada_hor1['values']=("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00")
    L3 = Label(frames_modi[0], text="Horario 2", fg="white", bg="black", font=("Times New Roman", 18))
    entrada_hor2 = ttk.Combobox(frames_modi[0], font=("Times New Roman", 20))
    entrada_hor2['values']=("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00")
    L4 = Label(frames_modi[0], text="Horario 3", fg="white", bg="black", font=("Times New Roman", 18))
    entrada_hor3 = ttk.Combobox(frames_modi[0], font=("Times New Roman", 20))
    entrada_hor3['values']=("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00")
    boton_confirmar = Button(frames_modi[0], text="Confirmar", font=("Times New Roman", 20), fg="white", bg="blue")

    # Crear botones en el frame_crear_peli
    boton_name = Button(frame_crear_peli, text="Ingresar Informacion de Pelicula", font=("Times New Roman", 20), fg="white", bg="blue", command=lambda: [mostrar_frame(frames_modi[0]), ingresar_nombre()])
    boton_name.pack(pady=30)

    boton_ima = Button(frames_modi[0], text="Ingresar Imagen De Pelicula", font=("Times New Roman", 20), fg="white", bg="blue", command=seleccionar_imagen)
    boton_ima.pack(pady=30)

    boton_regreso(frames_modi[0], frame_crear_peli)
    boton_regreso(frames_modi[2], frame_crear_peli)

    mostrar_frame(frame_crear_peli)

    root1.mainloop()

# Función para mostrar un frame específico
def mostrar_frame(frame):
    frame.tkraise()

# Crear contenedores (frames) para cada sección
def crear_frames(root, n, base_name):
    frames = []
    for i in range(n):
        frame_name = f"frame_{base_name}{i+1}"
        frame = Frame(root, bg="black", name=frame_name)  
        frame.place(x=0, y=0, width=1200, height=720)
        frames.append(frame)
    return frames

# Crear frame para crear peliculas


def boton_regreso(frame_f, frame):
    boton_volver1 = Button(frame_f, text="Volver", bg="black", fg="white", command=lambda: mostrar_frame(frame), font=("Times New Roman", 14))
    boton_volver1.place(x=10, y=675)

#Buscar id disponible en la base de datos
original_filename=""

def seleccionar_imagen():
    # Abre un cuadro de diálogo para seleccionar un archivo
    global ruta_archivo
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar una imagen",
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if ruta_archivo:
        # Crear un frame para agrupar la imagen y el botón
        frame_imagen = Frame(frame_crear_peli, bg="black")
        frame_imagen.pack(side=LEFT, padx=20)
        
        # Cargar la imagen utilizando PIL
        imagen = Image.open(ruta_archivo)
        imagen = imagen.resize((250, 250), Image.LANCZOS)  # Redimensionar la imagen
        imagen_tk = ImageTk.PhotoImage(imagen)
        
        # Crear y mostrar la etiqueta de la imagen
        etiqueta_imagen = Label(frame_imagen, bg="black", image=imagen_tk)
        etiqueta_imagen.image = imagen_tk  # Guardar una referencia a la imagen para evitar que se recoja como basura
        etiqueta_imagen.pack()

        # Crear y mostrar el botón con el nombre
        boton_nombre = Button(frame_imagen, text="", bg="blue", fg="white", font=("Times New Roman", 20))
        boton_nombre.pack(pady=10)

        global original_filename
        # Obtener el nombre del archivo seleccionado
        original_filename = os.path.basename(ruta_archivo)
        print(f"Archivo seleccionado: {original_filename}")

        # Especificar el nuevo nombre del archivo (mantener el nombre original)
        new_file_path = os.path.join(os.getcwd(), original_filename)

        # Copiar la imagen al directorio actual
        shutil.copy(ruta_archivo, new_file_path)
        print(f"Imagen guardada como: {new_file_path}")

        # Asignar la referencia del botón a una variable global para poder actualizar su texto después
        global boton_nombre_actual
        boton_nombre_actual = boton_nombre
    



def ingresar_nombre():
    # Mostrar las etiquetas y entradas de texto
    global entrada_nombre
    L.pack(pady=10)
    entrada_nombre.pack(pady=10)
    L2.pack(pady=10)
    entrada_hor1.pack(pady=10)
    L3.pack(pady=10)
    entrada_hor2.pack(pady=10)
    L4.pack(pady=10)
    entrada_hor3.pack(pady=10)
    boton_confirmar.pack(pady=10)
    

    boton_confirmar.config(command=insertar_pelicula)



# Mantener ventana abierta
def insertar_pelicula():
    global original_filename
    global entrada_hor1, entrada_hor2, entrada_hor3
    hor1="Funcion "+f"{entrada_hor1.get()}"
    hor2="Funcion "+f"{entrada_hor2.get()}"
    hor3="Funcion "+f"{entrada_hor3.get()}"

    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    fcursor=bd.cursor()
    sql="INSERT INTO prueba (id, pelicula, imagen, Horario1, Horario2, Horario3) VALUES ('{0}','{1}', '{2}','{3}','{4}','{5}')".format(IDD, entrada_nombre.get(),original_filename,hor1,hor2,hor3 )

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado", title="Aviso")
        print(IDD)
        print(entrada_nombre.get())
        print(original_filename)

    bd.close()

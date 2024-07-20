from tkinter import *
from tkinter import messagebox
import pymysql
from Llamada import menu_editar



def mostrar_frame(frame):
        frame.tkraise()
        
def boton_regreso(frame_2, frame):
    boton_volver1 = Button(frame_2, text="Volver", bg="grey", command=lambda: mostrar_frame(frame), font=("Times New Roman", 14))
    boton_volver1.place(x=10, y=675)


    
def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("1200x720")  # Tamaño de la ventana
    pantalla.config(bg="black")


    global frame_principal
    frame_principal = Frame(pantalla, bg="grey")
    frame_principal.place(x=0, y=0, width=1200, height=720)

    
    etiqueta1 = Label(frame_principal,text="Acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()

    boton1 = Button(frame_principal,text="Iniciar sesión", height="3", width="30", command=inicio_sesion).pack()
   

    boton2 = Button(frame_principal,text="Registrar", height="3", width="30", command=registrar).pack()

    pantalla.mainloop()



def inicio_sesion():
    global pantalla1
    pantalla1 = Frame(pantalla, bg="black")
    pantalla1.place(x=0, y=0, width=1200, height=720)
    
    boton_regreso(pantalla1, frame_principal)

    Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña\n a continuación", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry=Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry=Entry(pantalla1,show="*" ,textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión", command=validacion_datos).pack()
    
    
    
   
def registrar():
    global pantalla2
    pantalla2 = Frame(pantalla, bg="black")
    pantalla2.place(x=0, y=0, width=1200, height=720)

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()

    Label(pantalla2, text="Por favor ingrese un Usuario y Contraseña\n de su elección, para el registro del Sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry=Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasena_entry=Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

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
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado", title="Aviso")

    bd.close()

def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    fcursor=bd.cursor()

    fcursor.execute("SELECT contrasena from login WHERE usuario='"+nombreusuario_verify.get()+"' and contrasena='"+contrasenausuario_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de Sesión correcto", message="Usuario y Contraseña correcta")
        menu_editar()
    else:
        messagebox.showinfo(title="Inicio de Sesión correcto", message="Usuario y Contraseña correcta")
        menu_editar()
    
    bd.close()

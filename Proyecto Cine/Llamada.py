from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from Modo_Andmin import admin_pantalla as admin
from Modo_Andmin import original_filename

def menu_editar():
    global root
    # Crear variable para abrir ventana y nombre
    root = Tk()
    root.title("Cine")  # Nombre
    root.geometry("1200x720")  # Tamaño de la ventana
    root.config(bg="black")  # Color de la ventana

    global frame_principal, frame_admin, frame_primario, frames_primarios, frame_secundario, frames_secundarios, frame_terciario, frames_terciarios
    # Frame principal
    frame_principal = crear_frames(root, 1, "principal")[0]
    frame_admin=crear_frames(root, 1, "Admin")[0]

    # Crear 3 frames primarios
    frame_primario = crear_frames(root, 1, "primario")[0]
    frames_primarios = crear_frames(root, 3, "primario_funcion")

    # Crear 3 frames secundarios
    frame_secundario = crear_frames(root, 1, "secundario")[0]
    frames_secundarios = crear_frames(root, 3, "secundario_funcion")

    # Crear 3 frames terciarios
    frame_terciario = crear_frames(root, 1, "terciario")[0]
    frames_terciarios = crear_frames(root, 3, "terciario_funcion")

    # Crear botones para seleccionar salas en los frames

    bot(frame_primario, frames_primarios)
    bot(frame_secundario, frames_secundarios)
    bot(frame_terciario, frames_terciarios)

    # Agregar etiquetas y botones de regreso a los frames
    etiquetas_hora_funciones(frame_primario, "Spiderman \nNo Way \nHome", "Funcion 13:00", "Funcion 14:00", "Funcion 13:00")
    etiquetas_hora_funciones(frame_secundario, "Deadpool \nand \nWolverine", "Funcion 15:00", "Funcion 15:00", "Funcion 16:00")
    etiquetas_hora_funciones(frame_terciario, "Venom \nEl Ultimo \nBaile", "Funcion 17:00", "Funcion 18:00", "Funcion 18:00")

    boton_regreso(frame_primario, frame_admin)
    boton_regreso(frame_secundario, frame_admin)
    boton_regreso(frame_terciario, frame_admin)

    for mos_bot_r in range (3):
        boton_regreso(frames_primarios[mos_bot_r], frame_primario)
        boton_regreso(frames_secundarios[mos_bot_r], frame_secundario)
        boton_regreso(frames_terciarios[mos_bot_r], frame_terciario)

    #Etiquetas en el frame principal
    et1 = Label(frame_admin, bg="black", fg="white", font=("Times New Roman", 27), text="Funciones de Spiderman")
    et1.place(x=30, y=30)

    et2 = Label(frame_admin, bg="black", fg="white", font=("Times New Roman", 27), text="Funciones de Deadpool")
    et2.place(x=450, y=30)

    et3 = Label(frame_admin, bg="black", fg="white", font=("Times New Roman", 27), text="Funciones de Venom")
    et3.place(x=850, y=30)

    #Boton para entrar al editor de peliculas
    bot_admi=Button(frame_admin, text="Editar", command=lambda: admin(), fg="white", bg="blue", font=("Times New Roman", 27))
    bot_admi.place(x=90, y=10, height=70)

    # Botones para ingresar a los frames de peliculas
    bot1 = Button(frame_admin, text="Ingresar", command=lambda: mostrar_frame(frame_primario), fg="white", bg="blue", font=("Times New Roman", 27))
    bot1.place(x=90, y=600, width=200, height=70)

    bot2 = Button(frame_admin, text="Ingresar", command=lambda: mostrar_frame(frame_secundario), fg="white", bg="blue", font=("Times New Roman", 27))
    bot2.place(x=510, y=600, width=200, height=70)

    bot3 = Button(frame_admin, text="Ingresar", command=lambda: mostrar_frame(frame_terciario), fg="white", bg="blue", font=("Times New Roman", 27))
    bot3.place(x=910, y=600, width=200, height=70)

    global botones_1_funcion1, botones_1_funcion2, botones_1_funcion3
    global botones_2_funcion1, botones_2_funcion2, botones_2_funcion3
    global botones_3_funcion1, botones_3_funcion2, botones_3_funcion3
    botones_1_funcion1 = crear_matriz(frames_primarios[0], 1)
    botones_1_funcion2 = crear_matriz(frames_primarios[1], 2)
    botones_1_funcion3 = crear_matriz(frames_primarios[2], 3)

    # 2
    botones_2_funcion1 = crear_matriz(frames_secundarios[0], 1)
    botones_2_funcion2 = crear_matriz(frames_secundarios[1], 2)
    botones_2_funcion3 = crear_matriz(frames_secundarios[2], 3)

    # 3
    botones_3_funcion1 = crear_matriz(frames_terciarios[0], 1)
    botones_3_funcion2 = crear_matriz(frames_terciarios[1], 2)
    botones_3_funcion3 = crear_matriz(frames_terciarios[2], 3)

    mostrar_mejores(frames_primarios[0], botones_1_funcion1)
    mostrar_mejores(frames_primarios[1], botones_1_funcion2)
    mostrar_mejores(frames_primarios[2], botones_1_funcion3)

    mostrar_mejores(frames_secundarios[0], botones_2_funcion1)
    mostrar_mejores(frames_secundarios[1], botones_2_funcion2)
    mostrar_mejores(frames_secundarios[2], botones_2_funcion3)


    mostrar_mejores(frames_terciarios[0], botones_3_funcion1)
    mostrar_mejores(frames_terciarios[1], botones_3_funcion2)
    mostrar_mejores(frames_terciarios[2], botones_3_funcion3)

    # Llamadas a la función para cada imagen
    cargar_imagen("spidy1.jpg", 400, 500, frame_primario, 780, 50)
    cargar_imagen("imag1.jpg", 400, 500, frame_secundario, 780, 50)
    cargar_imagen("venom1.jpg", 400, 500, frame_terciario, 780, 50)

    cargar_imagen("spidy1.jpg", 350, 500, frame_admin, 30, 80)
    cargar_imagen("imag1.jpg", 350, 500, frame_admin, 440, 80)
    cargar_imagen("venom1.jpg", 350, 500, frame_admin, 830, 80)


    # Mostrar el frame principal (anteriormente secundario) al inicio
    mostrar_frame(frame_admin)

    root.mainloop()


# Función para mostrar un frame específico
def mostrar_frame(frame):
    frame.tkraise()

# Crear contenedores (frames) para cada sección
def crear_frames(root, n, base_name):
    frames = []
    for i in range(n):
        frame_name = f"frame_{base_name}{i+1}"
        frame = Frame(root, bg="black", name=frame_name)  # Añadir `name` para identificación
        frame.place(x=0, y=0, width=1200, height=720)
        frames.append(frame)
    return frames



# Función para crear botones en los frames de sala
def bot(frame, frame_funciones):
    for h in range(3):
        # Capturar el valor de `h` en el closure
        frame_funcion = frame_funciones[h]
        boton = Button(frame, text=f"Sala {h+1}", command=lambda f=frame_funcion: mostrar_frame(f), bg="black", fg="white", font=("Times New Roman", 25))
        boton.place(x=300, y=50 + 200 * h, width=200, height=100)


# Función de botón "volver"
def boton_regreso(frame_funcion, frame):
    boton_volver1 = Button(frame_funcion, text="Volver", bg="black", fg="white", command=lambda: mostrar_frame(frame), font=("Times New Roman", 14))
    boton_volver1.place(x=10, y=675)
    

def etiquetas_hora_funciones(frame, titulo, tex1, tex2, tex3):
    global contador
    global valor_guardado

    def contar_clics():
        global contador
        if contador == 25:
            messagebox.showinfo(message="Límite de asientos alcanzado", title="Aviso")
            END
        else:
            contador += 1
            label_contador.config(text=contador)

    def restar():
        global contador
        if contador > 0:
            contador -= 1
            label_contador.config(text=contador)
        else:
            END

    def confirmar():
        global valor_guardado
        valor_guardado = contador 
        if valor_guardado == 0:
            messagebox.showinfo(message="Elija entradas", title="Aviso")
        else:
            label_confirmacion.config(text=f"Entradas: {valor_guardado}")
            return valor_guardado

    # Inicializar el contador y valor final
    contador = 0
    valor_guardado = None
    

    etiqueta = Label(frame, text=titulo, bg="black", fg="white", font=("Times New Roman", 25))
    etiqueta.place(x=910, y=560)

    e_sala1 = Label(frame, text=tex1, bg="black", fg="white", font=("Times New Roman", 25))
    e_sala1.place(x=30, y=90)

    e_sala2 = Label(frame, text=tex2, bg="black", fg="white", font=("Times New Roman", 25))
    e_sala2.place(x=30, y=280)

    e_sala3 = Label(frame, text=tex3, bg="black", fg="white", font=("Times New Roman", 25))
    e_sala3.place(x=30, y=480)
    
    e_entradas = Label(frame, text="2D General ", bg="black", fg="white", font=("Times New Roman", 25))
    e_entradas.place(x=30, y=600)
    
    label_contador = Label(frame, text="0", bg="black", fg="white", font=("Times New Roman", 18))
    label_contador.place(x=348, y=599)
    
    boton_suma = Button(frame, text="+", bg="blue", fg="white", font=("Times New Roman", 20), command=contar_clics)
    boton_suma.place(x=390, y=590)
    
    boton_resta = Button(frame, text="-", bg="blue", fg="white", font=("Times New Roman", 20), command=restar)
    boton_resta.place(x=300, y=590)
    
    boton_confirmar = Button(frame, text="Confirmar", font=("Times New Roman", 20), fg="white", bg="blue", command=confirmar)
    boton_confirmar.place(x=600, y=590)
  
    label_confirmacion = Label(frame, text="Entradas: Ninguna",font=("Times New Roman", 20), fg="white", bg="black")
    label_confirmacion.place(x=400, y=670)
    print(valor_guardado)
    
    

# Matriz para almacenar las referencias de los botones en cada sala

def crear_matriz(frame, sala):
    def verificar_rojo():
        for fila in matriz_botones:
            for boton in fila:
                if boton["bg"] == "blue":
                    boton.config(bg="red", text="O")
                
    def verificar():
        for fila in matriz_botones:
            for boton in fila:
                if boton["bg"] == "yellow":
                    boton.config(bg="red", text="O")
                    
    def cambiar_color(boton):
        if boton["bg"] == "green":
            boton.config(bg="blue", text="R")
        elif boton["bg"] == "red":
            boton.config(state=DISABLED)
        elif boton["bg"]=="yellow":
            boton.config(bg="blue", text="R")
        else:
            boton.config(bg="green", text="L")
        
    matriz_botones = []  
    if sala ==1:
        fil = 5
        cul = 5
    elif sala==2:
        fil = 5
        cul = 5
    else:
        fil = 5
        cul = 5
        
    n_fila  =0 
    nasci = 64
    letras_filas = []
    numeros_filas = []   
     
    for i in range(fil):
        nasci += 1
        nasci= chr(nasci)
        fila_frame = Frame(frame, bg="black")
        fila_frame.pack()
        fila_botones = []
        
        n_fila+=1
        numeros_filas.append(n_fila)
        letras_filas.append(nasci)
        letras_filas.sort(reverse=True)
  
        for idx, letra in enumerate(letras_filas):
            etiq_1 = Label(frame, text=letra, font=("Arial", 20),fg="white", bg="black")
            etiq_1.place(x=40, y=55 + idx * 60)
        nasci = ord(nasci)
        
        for id, nf in enumerate(numeros_filas):
            etiq_2 = Label(frame, text=nf, font=("Arial", 20),fg="white", bg="black")
            etiq_2.place(x=100 + id * 90, y=10)
            
    
        for j in range(cul):
            
            boton = Button(frame, text="L", bg="green", font=("Times New Roman", 25))

            boton.config(command=lambda b=boton: cambiar_color(b))
                   
            boton.place(x=(j+0.80) * 90, y=(i+0.80) * 60, width=90, height=55)
            fila_botones.append(boton)

        matriz_botones.append(fila_botones)
        
    boton_volver1 = Button(frame, text="Reservar", bg="black",fg="white", font=("Times New Roman", 25), command=verificar_rojo)
    boton_volver1.place(x=795, y=290)

    botonr = boton_volver1 = Button(frame, text="Reservar Mejores \nAsientos ",fg="white", bg="black", font=("Times New Roman", 25), command=verificar)
    botonr.place(x=740, y=150)
    
    
    botoncol=Label(frame, bg="green", font=("Times New Roman", 15),fg="white", text="     ")
    botoncol.place(x=750, y=500)
    
    botmen=Label(frame, bg="black", font=("Times New Roman", 15),fg="white", text="Libre")
    botmen.place(x=815, y=500)
    
    botoncol=Label(frame, bg="red", font=("Times New Roman", 15),fg="white", text="     ")
    botoncol.place(x=750, y=550)
    
    botmen1=Label(frame, bg="black", font=("Times New Roman", 15),fg="white", text="Ocupado")
    botmen1.place(x=815, y=550)
    
    botoncol=Label(frame, bg="blue", font=("Times New Roman", 15),fg="white", text="     ")
    botoncol.place(x=750, y=600)
    botmen2=Label(frame, bg="black", font=("Times New Roman", 15),fg="white", text="Reservado")
    botmen2.place(x=815, y=600)
        
    return matriz_botones  # Necesitamos devolver la matriz de botones




# Función para actualizar y marcar los mejores asientos disponibles
def actualizar_mejores_asientos(matriz_botones):
    mejores_asientos = []
    def es_disponible(fila, columna):
        return matriz_botones[fila][columna]["bg"] == "green"

    # Función para marcar los asientos como mejores
    def marcar_mejor_asiento(fila, columna):
        matriz_botones[fila][columna].config(bg="yellow", text="M")
        mejores_asientos.append((fila, columna))
    
    for J in range(4,-1,-1):
        if es_disponible(J,2):
            marcar_mejor_asiento(J,2)
            break
        elif es_disponible(J,3) and es_disponible(J,1):
            marcar_mejor_asiento(J,3)
            marcar_mejor_asiento(J,1)
            break
        elif es_disponible(J,3):
            marcar_mejor_asiento(J,3)
            break
        elif es_disponible(J,1):
            marcar_mejor_asiento(J,1)
            break
        elif es_disponible(J,4) and es_disponible(J,0):
            marcar_mejor_asiento(J,4)
            marcar_mejor_asiento(J,0)
            break
        elif es_disponible(J,4):
            marcar_mejor_asiento(J,4)
            break
        elif es_disponible(J,0):
            marcar_mejor_asiento(J,0)
            break

    return mejores_asientos


def mostrar_mejores(frame,boton):
    def mostrar_mejores_asientos():
        mejores_asientos = actualizar_mejores_asientos(boton)  # Ejemplo: usando la matriz de la primera función del primer frame
    # Suponiendo que tienes una etiqueta para mostrar los mejores asientos en tu interfaz gráfico
        if mejores_asientos:
            mensaje = "Los mejores asientos son:\n"
            for J in range(4,-1,-1):
                A=69-J
                if mejores_asientos==[(J,2)]:
                    mensaje += f"Fila {chr(A)}, Columna {3}\n"
                    break
                elif mejores_asientos==[(J,3), (J,1)]:
                    mensaje += f"Fila {chr(A)}, Columna {2} y {4}\n"
                    break
                elif mejores_asientos==[(J,1)]:
                    mensaje += f"Fila {chr(A)}, Columna {2}\n"
                    break
                elif mejores_asientos==[(J,3)]:
                    mensaje += f"Fila {chr(A)}, Columna {4}\n"
                    break
                elif mejores_asientos==[(J,4), (J,0)]:
                    mensaje += f"Fila {chr(A)}, Columna {5} y {1}+1\n"
                    break
                elif mejores_asientos==[(J,4)]:
                    mensaje += f"Fila {chr(A)}, Columna {5}\n"
                    break
                elif mejores_asientos==[(J,0)]:
                    mensaje += f"Fila {chr(A)}, Columna {1}\n"
                    break
                
            
        else:
            label_mejores_asientos.config(text="No hay mejores asientos disponibles.")
    label_mejores_asientos = Label(frame, text="",fg="white", bg="black", font=("Times New Roman", 28))
    label_mejores_asientos.place(x=50, y=540)

    # Suponiendo que tienes un botón en tu interfaz que al presionarlo se llama mostrar_mejores_asientos
    boton_mostrar_mejores = Button(frame, text="Mostrar Mejores \nAsientos",font=("Times New Roman", 25),fg="white", bg="black", command=mostrar_mejores_asientos)
    boton_mostrar_mejores.place(x=740, y=10)





def cargar_imagen(ruta, ancho, alto, frame, x, y):
    
    pil_image = Image.open(ruta)
    pil_image = pil_image.resize((ancho, alto))
    tk_image = ImageTk.PhotoImage(pil_image)
    
    label = Label(frame, image=tk_image)
    label.image = tk_image  # Necesario para evitar que la imagen sea eliminada por el recolector de basura
    label.place(x=x, y=y)

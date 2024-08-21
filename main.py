import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry
from PIL import Image, ImageTk
import random
import string
from datetime import datetime
from tkinter import ttk
from tkinter import simpledialog
import csv

# Variable para controlar el estado del bucle
correr = True

#precio de entrada
costo = 125

# Obtener la fecha actual
fecha_actual = datetime.now()

contraseña = "12345"

diccionario = { 
    'E074ABC12': ('2024-08-19', '14:30:00', 'prueba', '0', 0),
}

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema del Museo")
ventana.geometry("800x600")

# Agregar un widget de etiqueta
etiqueta = tk.Label(ventana, text="¡Museo de Antropología e Historia!", font=("Arial", 14))
etiqueta.pack(pady=20)

# Estado inicial
estado = tk.StringVar(value="inactivo")

# Cargar y redimensionar la imagen usando PIL
try:
    imagen_original = Image.open("imagen.png")
    imagen_redimensionada = imagen_original.resize((200, 200))
    imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
except FileNotFoundError:
    print("Error: No se pudo encontrar la imagen.")
    ventana.destroy()

# Crear un contenedor para la imagen y los botones
frame = tk.Frame(ventana)
frame.pack(padx=20, pady=20)

# Crear un widget de etiqueta que contenga la imagen
etiqueta_imagen = tk.Label(frame, image=imagen_tk)
etiqueta_imagen.pack(side="left", padx=10)



def cerrar_programa():
    global correr
    correr = False  # Cambiar el estado para salir del bucle
    ventana.destroy()



def configurar(popupwindow):
    print("hola")
    nombre = entry_nombre.get() 
    #print(f"Nombre: {nombre}")
    
    if nombre == contraseña:
        boton2.config(state="normal")
        boton3.config(state="normal")
        popupwindow.destroy()
    else:
        popupwindow = Toplevel(ventana)
        popupwindow.title("Error")
        popupwindow.geometry("600x400")

        alert = Label(popupwindow, text="Error ingresa de nuevo la contraseña:")
        alert.pack(pady=10)
        button1 = Button(popupwindow, text="OK", command=popupwindow.destroy)
        button1.pack(pady=10)
        

def mostrar_tabla(popupwindow):
    print("hola")
    nombre = entry_nombre.get() 
    #print(f"Nombre: {nombre}")
    
    if nombre == contraseña:
        popupwindow.destroy()
        tabla()
        boton2.config(state="disabled")
        boton3.config(state="disabled")
    else:
        popupwindow = Toplevel(ventana)
        popupwindow.title("Error")
        popupwindow.geometry("600x400")

        alert = Label(popupwindow, text="Error ingresa de nuevo la contraseña:")
        alert.pack(pady=10)
        button1 = Button(popupwindow, text="OK", command=popupwindow.destroy)
        button1.pack(pady=10)


def tabla():
    popupwindow = Toplevel(ventana)
    popupwindow.title("Alert")
    popupwindow.geometry("600x400")

    alert = Label(popupwindow, text="Estas fueron las visitas del dia de hoy :")
    alert.pack(pady=10)

    # Crear el widget Treeview
    tv = ttk.Treeview(popupwindow, columns=("Folio", "Fecha", "Hora", "Nombre", "Edad", "Ganancia"), show="headings")
    
    # Definir los encabezados de las columnas
    tv.heading("Folio", text="Folio")
    tv.heading("Fecha", text="Fecha")
    tv.heading("Hora", text="Hora")
    tv.heading("Nombre", text="Nombre")
    tv.heading("Edad", text="Edad")
    tv.heading("Ganancia", text="Ganancia")

    # Definir el ancho de las columnas
    tv.column("Folio", width=80)
    tv.column("Fecha", width=100)
    tv.column("Hora", width=80)
    tv.column("Nombre", width=150)
    tv.column("Edad", width=30)
    tv.column("Ganancia", width=30)
    
    # Agregar datos del diccionario a la tabla
    suma_ganancias = 0

    # Agregar datos del diccionario a la tabla
    for folio, (fecha, hora, nombre, edad, ganancia) in diccionario.items():
        tv.insert("", tk.END, values=(folio, fecha, hora, nombre, edad, ganancia))
        suma_ganancias += ganancia  # Sumar las ganancias
    
    # Insertar una fila al final con la suma total de las ganancias
    tv.insert("", tk.END, values=("", "", "", "", "Total", suma_ganancias))

    tv.pack(pady=10, fill=tk.BOTH, expand=True)

    button1 = Button(popupwindow, text="OK", command=popupwindow.destroy)
    button1.pack(pady=10)
    button2 = Button(popupwindow, text="DESCARGAR", command=guardar_en_csv)
    button2.pack(side="left",pady=10)


# Definir funciones para los botones
def iniciar():
    popupwindow = Toplevel(ventana)
    popupwindow.title("Alert")
    popupwindow.geometry("600x400")

    alert = Label(popupwindow, text="Ingrese la contraseña para iniciar:")
    alert.pack(pady=10)

   # Etiqueta y campo de entrada para 
    label_nombre = Label(popupwindow, text="Contraseña:")
    label_nombre.pack(pady=5)
    global entry_nombre
    entry_nombre = Entry(popupwindow, width=25)
    entry_nombre.pack(pady=5)

    button1 = Button(popupwindow, text="OK", command=lambda: configurar(popupwindow))
    button1.pack(pady=10)

def nuevo_visitante():
    popupwindow = Toplevel(ventana)
    popupwindow.title("Alert")
    popupwindow.geometry("600x400")

    alert = Label(popupwindow, text="Ingrese información:")
    alert.pack(pady=10)



   # Etiqueta y campo de entrada para Nombre
    label_nombre = Label(popupwindow, text="Nombre:")
    label_nombre.pack(pady=5)
    global entry_nombre
    entry_nombre = Entry(popupwindow, width=25)
    entry_nombre.pack(pady=5)

    # Etiqueta y campo de entrada para Edad
    label_edad = Label(popupwindow, text="Edad:")
    label_edad.pack(pady=5)
    global entry_edad
    entry_edad = Entry(popupwindow, width=25)
    entry_edad.pack(pady=5)

    # Variable asociada al Checkbutton
    checkbox_value = tk.BooleanVar()

    # Crear el Checkbutton dentro de la ventana emergente
    checkbox = tk.Checkbutton(popupwindow, text="Es maestro o Estudiante", variable=checkbox_value)
    checkbox.pack(pady=10)

    # Asignar la función de cierre
    popupwindow.protocol("WM_DELETE_WINDOW", lambda: print(f"Checkbox estado: {checkbox_value.get()}"))


    # Etiqueta y campo de entrada para Edad
    label_dinero = Label(popupwindow, text="$ Recibe:")
    label_dinero.pack(pady=5)
    global entry_dinero
    entry_dinero = Entry(popupwindow, width=25)
    entry_dinero.pack(pady=5)



    button1 = Button(popupwindow, text="OK", command=lambda: mostrar_datos(popupwindow, checkbox_value.get()))
    button1.pack(pady=10)

def cerrar_corte():
    popupwindow = Toplevel(ventana)
    popupwindow.title("Alert")
    popupwindow.geometry("600x400")

    alert = Label(popupwindow, text="Ingrese la contraseña para acceder al corte:")
    alert.pack(pady=10)

   # Etiqueta y campo de entrada para 
    label_nombre = Label(popupwindow, text="Contraseña:")
    label_nombre.pack(pady=5)
    global entry_nombre
    entry_nombre = Entry(popupwindow, width=25)
    entry_nombre.pack(pady=5)

    button1 = Button(popupwindow, text="OK", command=lambda: mostrar_tabla(popupwindow))
    button1.pack(pady=10)
    #tabla()




def generar_folio():
    #print("Llamé a generar_folio")
    
    # Generar un folio aleatorio único
    chars = string.ascii_uppercase + string.digits
    folio = "E074"  # Prefijo fijo
    for _ in range(5):
        folio += random.choice(chars)
    
    # Imprimir el folio generado
    print(folio)
    #print(diccionario["id"][0])
    
    # Retornar el folio
    return folio

def guardar_en_csv():
    suma_ganancias = 0

    
    
    # Guardar los datos del diccionario en un archivo CSV
    with open('datos.csv', mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Folio', 'Fecha', 'Hora', 'Nombre', 'Edad', 'Ganancia'])  # Escribir los encabezados
        for folio, (fecha, hora, nombre, edad, ganancia) in diccionario.items():
            escritor.writerow([folio, fecha, hora, nombre, edad, ganancia])  # Escribir cada fila de datos
            suma_ganancias += ganancia  # Sumar las ganancias
        
        # Agregar la fila de total de ganancias
        escritor.writerow(['', '', '', '', 'Total', suma_ganancias])

    print("Datos guardados en datos.csv")
    

def mostrar_datos(popupwindow, checkbox):
    # Formatear la fecha
    fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
    fecha_hora = fecha_actual.strftime("%H:%M:%S")
    #print("Fecha y hora formateada:", fecha_formateada)
    nombre = entry_nombre.get()
    edad = int(entry_edad.get())
    dinero = float(entry_dinero.get())
    folio = str(generar_folio())
    check = checkbox

    descuento = 0

    if (edad <= 3):
        descuento = 1.0
    elif (edad >= 60):
        descuento = 0.12
    elif (check == True):
        descuento = 0.10
    else:
        descuento = 0
    
    cant_des = costo * descuento

    ganancia = costo - cant_des

    print("folio", folio)
    print(f"Nombre: {nombre}")

    popupwindow.destroy()
    diccionario[folio] = (fecha_formateada, fecha_hora,  nombre, edad, ganancia)
    print(diccionario)


# Crear botones al lado de la imagen
#boton1 = tk.Button(frame, text="Iniciar", command=iniciar)
#boton1.pack(side="top", pady=5)

#boton2 = tk.Button(frame, text="Nuevo Visitante", command=nuevo_visitante, state="disabled")
#boton2.pack(side="top", pady=5)

boton2 = tk.Button(frame, text="Nuevo Visitante", command=nuevo_visitante, state="disabled")
boton2.pack(side="top", pady=5)

boton3 = tk.Button(frame, text="Cerrar Corte", command=cerrar_corte, state="disabled")
boton3.pack(side="top", pady=5)

# Crear un botón para cerrar el programa
boton_cerrar = tk.Button(ventana, text="Cerrar Programa", command=cerrar_programa)
boton_cerrar.pack(pady=20)


# Crear el widget Treeview
tv = ttk.Treeview(ventana, columns=("Tipo de visitante", "Descuento"), show="headings")

# Definir los encabezados de las columnas
tv.heading("Tipo de visitante", text="Tipo de visitante")
tv.heading("Descuento", text="Descuento")


# Definir el ancho de las columnas
tv.column("Tipo de visitante", width=150)
tv.column("Descuento", width=100)


# Valores fijos para la tabla
datos = [
    ('Menores <3', '100%'),
    ('Adulto mayor >60', '12%'),
    ('Profesor', '10%'),
    ('Estudiante', '10%')
]

# Agregar los datos fijos a la tabla
for fila in datos:
    tv.insert("", tk.END, values=fila)

tv.pack(pady=10, fill=tk.BOTH, expand=True)


def procesamiento_datos():
    global correr
    while correr:
        # Preguntar al usuario si desea continuar o cerrar
        respuesta = simpledialog.askstring("Input", "contraseña:")
        if respuesta is None:
            respuesta = ""  # Si se cancela el diálogo, considera la respuesta como vacía
        
        if respuesta == contraseña:
            print("Adiós")
            correr = False
            boton2.config(state="normal")
            boton3.config(state="normal")
            break  # Salir del bucle
        elif respuesta != contraseña:
            print("Continuando...")
            continue  # Continuar con la siguiente iteración del bucle
        else:
            print("Entrada no válida. Continuando...")

# Iniciar el procesamiento de datos en un hilo separado
ventana.after(0, procesamiento_datos)

# Iniciar el bucle principal de tkinter
ventana.mainloop()

print("Ventana cerrada.")


#instalacion de librerias necesarias
#pip install mysql-connector-python
#pip install pymysql

import pymysql
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    user='root',
    password='Alumno123',
    host='localhost',
    database='citasmedicas')
#comprobacion de que la conexion funciona

cursor = conn.cursor()
cursor.execute("SELECT * FROM paciente_datos_personales")
resultados = cursor.fetchall()
for x in resultados:
  print(x)


def create_paciente():
    #se agregan los datos del formulario
    nombre = nombre_entry.get()
    apellido_paterno = apellido_paterno_entry.get()
    apellido_materno = apellido_materno_entry.get()
    telefono = telefono_entry.get()
    correoe = correoe_entry.get()
    fnacimiento = fnacimiento_entry.get()

    query = "INSERT INTO paciente_datos_personales (nombre, apellido_paterno, apellido_materno, telefono, correoe, fnacimiento) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, apellido_paterno, apellido_materno, telefono, correoe, fnacimiento))
    conn.commit()
    # mostramos un mensaje
    messagebox.showinfo("Completo","Paciente registrado con éxito")
    
    
def read_paciente():
    query = "SELECT * FROM paciente"
    cursor.execute(query)
    pacientes = cursor.fetchall()
    messagebox.showinfo("Pacientes", str(pacientes))

def update_paciente():
    #se agregan los datos del formulario
    nombre = nombre_entry.get()
    apellido_paterno = apellido_paterno_entry.get()
    apellido_materno = apellido_materno_entry.get()
    telefono = telefono_entry.get()
    correoe = correoe_entry.get()
    fnacimiento = fnacimiento_entry.get()

    query = "UPDATE paciente SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, telefono = %s, correoe = %s, fnacimiento = %s WHERE nombre = %s"
    cursor.execute(query, (nombre, apellido_paterno, apellido_materno, telefono, correoe, fnacimiento, nombre))
    conn.commit()
    messagebox.showinfo("Paciente actualizado con éxito")

def delete_paciente():
    #se agregan los datos del formulario
    nombre = nombre_entry.get()

    query = "DELETE FROM paciente WHERE nombre = %s"
    cursor.execute(query, (nombre,))
    conn.commit()
    messagebox.showinfo("Paciente eliminado con éxito")    
    
# Crear interfaz gráfica de usuario
root = tk.Tk()
root.title("CRUD Pacientes")

# Crear etiquetas y entradas de texto
nombre_label = tk.Label(root, text="Nombre:")
nombre_label.grid(row=0, column=0)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1)

apellido_paterno_label = tk.Label(root, text="Apellido Paterno:")
apellido_paterno_label.grid(row=1, column=0)
apellido_paterno_entry = tk.Entry(root)
apellido_paterno_entry.grid(row=1, column=1)

apellido_materno_label = tk.Label(root, text="Apellido Materno:")
apellido_materno_label.grid(row=2, column=0)
apellido_materno_entry = tk.Entry(root)
apellido_materno_entry.grid(row=2, column=1)

telefono_label = tk.Label(root, text="Teléfono:")
telefono_label.grid(row=3, column=0)
telefono_entry = tk.Entry(root)
telefono_entry.grid(row=3, column=1)

correoe_label = tk.Label(root, text="Correo electrónico:")
correoe_label.grid(row=4, column=0)
correoe_entry = tk.Entry(root)
correoe_entry.grid(row=4, column=1)

fnacimiento_label = tk.Label(root, text="Fecha de nacimiento:")
fnacimiento_label.grid(row=5, column=0)
fnacimiento_entry = tk.Entry(root)
fnacimiento_entry.grid (row=5, column=1)
boton_crear = tk.Button(root, text="Ingresar paciente")
boton_crear.grid(row=6, column=0)

boton_leer = tk.Button(root, text="Leer")
boton_leer.grid(row=6, column=1)

boton_actualizar = tk.Button(root, text="Actualizar")
boton_actualizar.grid(row=7, column=0)

boton_eliminar = tk.Button(root, text="Eliminar")
boton_eliminar.grid(row=7, column=1)

boton_crear.config(command=create_paciente)
boton_leer.config(command=read_paciente)
boton_actualizar.config(command=update_paciente)
boton_eliminar.config(command=delete_paciente)

root.mainloop()
conn.close()
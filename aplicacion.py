#instalacion de librerias necesarias
#pip install mysql-connector-python
#pip install pymysql
import re
from datetime import datetime
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

"""cursor = conn.cursor()
cursor.execute("SELECT * FROM paciente_datos_personales")
resultados = cursor.fetchall()
for x in resultados:
  print(x)"""

def validarCurp(Curp):
    while True:
        if len(Curp) !=18:
            print("Error, no se capturo correctamente el curp")
            Curp = input("Por favor, ingrese su curp:").upper()
        else:
            break
    return Curp
                
def validarTcelular(Tcelular):
    while True:
        if len(Tcelular) != 10 or not Tcelular.isdigit() :
            #probando if lo comente para tratar de reducirlo y solucionar error
            # if not Tcelular.isdigit():
            print("Error, no se capturo correctamente el celular, asegurese de que sean 10 digitos")
            Tcelular = input("Por favor, ingrese su telefono celular:")
        else:
            break
    return Tcelular
def validarCorreo(Correo):
    signos = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-z]{1,3}$")
    while True:
        if not signos.match(Correo):
            print("Error, el correo no tiene un formato valido")
            Correo = input("Por favor, ingrese su correo electronico:")
        else:
            break
    return Correo

def validarFecha(fecha):
     while True:
        try:
            fecha_validacion = datetime.strptime(fecha, "%Y-%m-%d")
            return fecha_validacion
        except ValueError:
            print("Fecha inválida. Por favor, ingrese una fecha en formato YYYY-MM-DD.")
            fecha = input("Ingresa una fecha tipo YYYY-MM-DD: ")
                       
def Paciente():
    print("""
-----Registre sus datos-----
1.Nombres
2.Apellido Paterno
3.Apellido Materno
4.Curp
5.Telefono celular
6.Correo Electronico
7.fecha de nacimiento
8.fecha de cita
9.hora de cita
10.sexo (H o M)
11.observaciones
        """)
    #12-id_formulario int auto_increment primary key
    while True:
        
        
        print("Puedes escribir salir en la siguiente pregunta para salir ")
        Nombres = input("Por favor, ingrese sus nombres:")
        if Nombres.lower()=="salir":
            print("Saliendo...")
            return
        Apaterno = input("Por favor, ingrese su apellido paterno: ")
        Amaterno = input("Por favor, ingrese su apellido materno: ")
        Nombres_Format=Nombres.replace(" ","")
        if not Nombres_Format.isalpha() or not Apaterno.isalpha() or not Amaterno.isalpha():
            print("Error, verifica que la informacion ingresada contenga solo letras y los apellidos sin espacios")
            continue
        #Validar la longitud-----*
        Curp = input("Por favor, ingrese su curp:").upper()
        Curp_validacion=validarCurp(Curp)
        
        Tcelular = input("Por favor, ingrese su telefono celular:")
        Tcelular_validacion=validarTcelular(Tcelular)
        Correo = input("Por favor, ingrese su correo electronico:")
        Correo_validacion= validarCorreo(Correo)
        
        fecha = input("Ingresa una fecha tipo YYYY-MM-DD:")
        fecha_validacion = validarFecha(fecha)
        
        
        #Fechas para agendar cita
    
        print("------------------------------")
        print("Se muestran tus datos ingresados")
        print(f"CURP: {Curp_validacion}")
        print(f"Nombres: {Nombres}")
        print(f"Apellido Paterno: {Apaterno}")
        print(f"Apellido Materno: {Amaterno}")
        print(f"Teléfono: {Tcelular_validacion}")
        print(f"Correo Electrónico:{Correo_validacion}")
        print(f"Fecha cita:  {fecha_validacion}")

        # print(listaPacientes)
        print("------------------------------")
        break

def menuPrincipal():
    while True:
      
        print(
            """
Bienvenido al sistema de citas médicas
“Por favor, identifícate”
Paciente (Agendar una cita)
Médico (Entrar al portal)

            """
        )
        print ("1 ) Paciente")
        print ("2 ) Doctor")
        print ("3 ) Salir")

        opcion = input("Ingrese la opcion que desea\n")

        if opcion == "1":
            Paciente()
        elif opcion == "2":
            Doctor()
        elif opcion == "3":
            
            print("Gracias Por usar el sistema de citas, que tenga un buen dia!")
            break
        else:
            print("-----------------------------")
            print("Opcion NO valida, favor de intentar de nuevo!")


menuPrincipal() 




"""def create_paciente():
    #se agregan los datos del formulario
 

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
    

    query = "UPDATE paciente SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, telefono = %s, correoe = %s, fnacimiento = %s WHERE nombre = %s"
    cursor.execute(query, (nombre, apellido_paterno, apellido_materno, telefono, correoe, fnacimiento, nombre))
    conn.commit()
    messagebox.showinfo("Paciente actualizado con éxito")

def delete_paciente():
    #se agregan los datos del formulario
    nombre = nombre_datos()

    query = "DELETE FROM paciente WHERE nombre = %s"
    cursor.execute(query, (nombre,))
    conn.commit()
    messagebox.showinfo("Paciente eliminado con éxito")    
"""


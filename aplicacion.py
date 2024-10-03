#instalacion de librerias necesarias
#pip install mysql-connector-python
#pip install pymysql
import re
from datetime import datetime
import pymysql

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
"""for x in resultados:
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
1.Curp
2.Nombres
3.Apellido Paterno
4.Apellido Materno
5.Telefono celular
6.Correo Electronico
7.fecha de nacimiento
8.fecha de cita
9.hora de cita
10.sexo (H o M)
11.observaciones
        """)
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
        
        fecha_nacimiento = input("Ingresa una fecha tipo YYYY-MM-DD: ") 
        fecha = input("Ingresa una fecha tipo YYYY-MM-DD: ")
        fecha_validacion = validarFecha(fecha)
        
        hora_cita = input ("Ingresa una hora tipo HH:MM:SS:")
        sexo_paciente = input ("H o M: ")
        observaciones= input("Escriba las observaciones que presente como alergias  o enfermedades: ")
        
    
        print("------------------------------")
        print("Se muestran tus datos ingresados")
        print(f"CURP: {Curp_validacion}")
        print(f"Nombres: {Nombres}")
        print(f"Apellido Paterno: {Apaterno}")
        print(f"Apellido Materno: {Amaterno}")
        print(f"Teléfono: {Tcelular_validacion}")
        print(f"Correo Electrónico:{Correo_validacion}")
        print(f"Fecha Nacimiento: {fecha_nacimiento}")
        print(f"Fecha cita:{fecha_validacion}")
        print(f"Fecha cita:{hora_cita}")
        print(f"Fecha cita:{sexo_paciente}")
        print(f"Fecha cita:{observaciones}")
        # print(listaPacientes)
        print("------------------------------")
        query = "insert into formulario (curp, nombre, apellido_paterno, apellido_materno, telefono, fnacimiento ,fecha, hora, sexo, correoe, observaciones) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
        cursor.execute(query, (Curp_validacion, Nombres, Apaterno, Amaterno, Tcelular_validacion, fecha_nacimiento, fecha_validacion, hora_cita, sexo_paciente, Correo_validacion, observaciones))
        conn.commit()
        print("Tu cita ha sido cargada")
        break

def Doctor():
     while True:
        print("""
-----Menu del Doctor-----
1. Enviar paciente a consultorio
2. Buscar expediente
3. Actualizar expediente
4. Eliminar paciente de citas
5. Salir
        """)
        opcion = input("Ingrese la opción que desea: ")
        
        if opcion == "1":
            curp_paciente = input("Ingrese el CURP del paciente: ")
            query = "SELECT * FROM formulario WHERE curp = %s"
            cursor.execute(query, (curp_paciente,))
            paciente = cursor.fetchone()
            if paciente:
                print("Paciente encontrado. Enviando a consultorio...")
                # Aquí puedes agregar la lógica para enviar al paciente a un consultorio
                print("Paciente enviado a consultorio con éxito.")
            else:
                print("Paciente no encontrado.")
        elif opcion == "2":
            nombre_paciente = input("Ingrese el nombre del paciente: ")
            query = "SELECT id_paciente FROM paciente_datos_personales WHERE nombre = %s"
            cursor.execute(query, (nombre_paciente,))
            paciente = cursor.fetchone()
            if paciente:
                id_paciente = paciente[0]
                query = "SELECT * FROM expediente WHERE id_paciente = %s"
                cursor.execute(query, (id_paciente,))
                expediente = cursor.fetchone()
                if expediente:
                    print("Expediente encontrado. Mostrando información...")
                    print(f"ID Expediente: {expediente[0]}")
                    print(f"ID Paciente: {expediente[1]}")
                    print(f"ID Cita: {expediente[2]}")
                    print(f"Fecha: {expediente[3]}")
                    print(f"Diagnóstico: {expediente[4]}")
                    print(f"Tratamiento: {expediente[5]}")
                    print(f"Observaciones: {expediente[6]}")
                else:
                    print("Expediente no encontrado.")
            else:
                print("Paciente no encontrado.")
        
        elif opcion == "3":
            id_cita = input("Ingrese el ID de la cita: ")
            query = "SELECT * FROM cita WHERE id_cita = %s"
            cursor.execute(query, (id_cita,))
            cita = cursor.fetchone()
            if cita:
                id_paciente = cita[1]
                id_medico = cita[2]
                fecha = cita[3]
                motivo = cita[4]
                estado = cita[5]
        
                print("Cita encontrada. Mostrando información...")
                print(f"ID Cita: {cita[0]}")
                print(f"ID Paciente: {cita[1]}")
                print(f"ID Médico: {cita[2]}")
                print(f"Fecha: {cita[3]}")
                print(f"Motivo: {cita[4]}")
                print(f"Estado: {cita[5]}")
        
                # Preguntar por la información del expediente
                diagnostico = input("Ingrese el diagnóstico: ")
                tratamiento = input("Ingrese el tratamiento: ")
                observaciones = input("Ingrese las observaciones: ")

                # Agregar al expediente
                query = "INSERT INTO expediente (id_paciente, id_cita, fecha, diagnostico, tratamiento, observacion) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (id_paciente, id_cita, fecha, diagnostico, tratamiento, observaciones))
                conn.commit()

                print("Expediente llenado con éxito.")
            else:
                print("Cita no encontrada.")
        elif opcion == "4":
            id_formulario = input("Ingrese el ID del formulario: ")
            query = "SELECT * FROM formulario WHERE id_formulario = %s"
            cursor.execute(query, (id_formulario,))
            formulario = cursor.fetchone()
            if formulario:
                print("Formulario encontrado. Mostrando información...")
                print(f"ID Formulario: {formulario[0]}")
                print(f"CURP: {formulario[1]}")
                print(f"Nombres: {formulario[2]}")
                print(f"Apellido Paterno: {formulario[3]}")
                print(f"Apellido Materno: {formulario[4]}")
                print(f"Teléfono: {formulario[5]}")
                print(f"Correo Electrónico: {formulario[6]}")
                print(f"Fecha Nacimiento: {formulario[7]}")
                print(f"Fecha cita: {formulario[8]}")
                print(f"Hora cita: {formulario[9]}")
                print(f"Sexo: {formulario[10]}")
                print(f"Observaciones: {formulario[11]}")

                eliminar_formulario = input("¿Desea eliminar el formulario? (S/N): ")
                if eliminar_formulario.upper() == "S":
                    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
                    conn.commit()
                    query = "DELETE FROM formulario WHERE id_formulario = %s"
                    cursor.execute(query, (id_formulario,))
                    conn.commit()
                 
                    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
                    conn.commit()
                    print("Formulario eliminado con éxito.")
                else:
                     print("Formulario no eliminado.")
            else:
                print("Formulario no encontrado.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Favor de intentar de nuevo.")
            
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


#codigo descartado por no ser usado para interfaz

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


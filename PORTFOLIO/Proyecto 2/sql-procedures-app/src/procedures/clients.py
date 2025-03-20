import mysql.connector
from db.connection import obtener_conexion

def mostrar_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.callproc('VerClientes')
    for result in cursor.stored_results():
        for row in result.fetchall():
            print(row)
    cursor.close()
    conexion.close()

def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('RegistrarCliente', (nombre, email, telefono, direccion))
        conexion.commit()
        print("Cliente agregado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def actualizar_cliente():
    id_cliente = input("Ingrese el ID del cliente a actualizar: ")
    nombre = input("Ingrese el nuevo nombre del cliente: ")
    email = input("Ingrese el nuevo email del cliente: ")
    telefono = input("Ingrese el nuevo teléfono del cliente: ")
    direccion = input("Ingrese la nueva dirección del cliente: ")


    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('ActualizarCliente', (id_cliente, nombre, email, telefono, direccion))
        conexion.commit()
        print("Cliente actualizado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_cliente():
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('EliminarCliente', (id_cliente,))
        conexion.commit()
        print("Cliente eliminado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
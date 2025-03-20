from db.connection import obtener_conexion
import mysql.connector

def mostrar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.callproc('VerProductos')
    for result in cursor.stored_results():
        for row in result.fetchall():
            print(row)
    cursor.close()
    conexion.close()

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = input("Ingrese el precio del producto: ")
    stock = input("Ingrese el stock del producto: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('AgregarProducto', (nombre, descripcion, precio, stock))
        conexion.commit()
        print("Producto agregado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def actualizar_producto():
    id_producto = input("Ingrese el ID del producto a actualizar: ")
    nombre = input("Ingrese el nuevo nombre del producto: ")
    descripcion = input("Ingrese la nueva descripción del producto: ")
    precio = input("Ingrese el nuevo precio del producto: ")
    stock = input("Ingrese el nuevo stock del producto: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('ActualizarProducto', (id_producto, nombre, descripcion, precio, stock))
        conexion.commit()
        print("Producto actualizado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_producto():
    id_producto = input("Ingrese el ID del producto a eliminar: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('EliminarProducto', (id_producto,))
        conexion.commit()
        print("Producto eliminado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
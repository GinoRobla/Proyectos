from db.connection import obtener_conexion
import mysql.connector


def mostrar_ordenes_por_cliente():
    id_cliente = input("Ingrese el ID del cliente: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('MostrarOrdenesPorCliente', [id_cliente])
        for result in cursor.stored_results():
            for row in result.fetchall():
                print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def reporte_producto_mas_vendido():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('ReporteProductoMasVendido')
        for result in cursor.stored_results():
            for row in result.fetchall():
                print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def clientes_con_mas_ordenes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.callproc('ClientesConMasOrdenes')
        for result in cursor.stored_results():
            for row in result.fetchall():
                print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
from colorama import Fore, Back, init
import mysql.connector

password = 'utntup'

#menus

def menu_principal():
    while True:
        print(Fore.YELLOW + "Menú Principal:")
        print(Fore.LIGHTCYAN_EX + "1. Gestión de Clientes")
        print(Fore.LIGHTGREEN_EX + "2. Gestión de Productos")
        print(Fore.LIGHTMAGENTA_EX + "3. Menú de Órdenes")
        print(Fore.LIGHTBLUE_EX + "4. Búsquedas Avanzadas")
        print(Fore.LIGHTRED_EX + "0. Salir")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if opcion == 1:
            menu_clientes()
        elif opcion == 2:
            menu_productos()
        elif opcion == 3:
            menu_ordenes()
        elif opcion == 4:
            menu_busquedas()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

#menu clientes

def menu_clientes():
    while True:
        print(Fore.BLACK + Back.LIGHTCYAN_EX + "Menú de Clientes:")
        print(Fore.LIGHTCYAN_EX + "1. Mostrar todos los clientes")  
        print(Fore.LIGHTCYAN_EX + "2. Registrar nuevo cliente")
        print(Fore.LIGHTCYAN_EX + "3. Actualizar informacion de un cliente")
        print(Fore.YELLOW + "0. Volver al menú principal")

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            mostrar_clientes()
        elif opcion == 2:
            agregar_cliente()
        elif opcion == 3:
            actualizar_cliente()
        #elif opcion == 4:
        #   eliminar_cliente(cliente_id)
        elif opcion == 0:
            break
        else:
            print("Opción no válida. Intenta nuevamente.")




#menu producto

def menu_productos():
    while True:
        print(Fore.BLACK + Back.LIGHTGREEN_EX + "Menú de Productos:")
        print(Fore.LIGHTGREEN_EX + "1. Ver productos")
        print(Fore.LIGHTGREEN_EX + "2. Agregar producto")
        print(Fore.LIGHTGREEN_EX + "3. Actualizar producto")
        print(Fore.LIGHTRED_EX + "4. Eliminar producto")
        print(Fore.YELLOW + "0. Volver al menu principal")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if opcion == 1:
            ver_productos()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 0:
            break
        else:
            print("Opción no válida. Intenta nuevamente.")



#menu ordenes

def menu_ordenes():
    while True:
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "Menú de Órdenes:")
        print(Fore.LIGHTMAGENTA_EX + "1. Mostrar ordenes por cliente")
        print(Fore.LIGHTMAGENTA_EX + "2. Modificar valor de un producto")
        print(Fore.YELLOW + "0. Volver al Menú Principal")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if opcion == 1:
            mostrar_ordenes_por_cliente()
        elif opcion == 2:
            modificar_ordenes_producto()
        elif opcion == 0:
            break
        else:
            print("Opción no válida. Intenta nuevamente.")



#menu busquedas
def menu_busquedas():
    while True:
        print(Fore.BLACK + Back.LIGHTBLUE_EX + "Menú de Búsquedas Avanzadas:")
        print(Fore.LIGHTBLUE_EX + "1. Consultas sobre clientes")
        print(Fore.LIGHTBLUE_EX + "2. Consultas sobre productos")
        print(Fore.YELLOW + "0. Volver al Menú Principal")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if opcion == 1:
            menu_busquedas_clientes() 
        elif opcion == 2:
            menu_busquedas_productos()  
        elif opcion == 0:
            break  
        else:
            print("Opción no válida. Intenta nuevamente.")

def menu_busquedas_clientes():
    while True:
        print(Fore.BLACK + Back.LIGHTBLUE_EX + "Buscar clientes:")
        print(Fore.LIGHTCYAN_EX + "1. Buscar clientes con mas ordenes")
        print(Fore.YELLOW + "0. Volver al menú de búsquedas")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if opcion == 1:
            clientes_con_mas_ordenes()
        elif opcion == 0:
            break  
        else:
            print("Opción no válida. Intenta nuevamente.")

def menu_busquedas_productos():
    while True:
        print(Fore.BLACK + Back.LIGHTBLUE_EX + "Buscar Productos:")
        print(Fore.LIGHTGREEN_EX + "1. Buscar productos mas vendidos")
        print(Fore.LIGHTGREEN_EX + "2. Consultar stock de un producto")
        print(Fore.YELLOW + "0. Volver al Menú de Búsquedas")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if opcion == 1:
            reporte_producto_mas_vendido()
        elif opcion == 2:
            consultar_stock_producto()
        elif opcion == 0:
            break 
        else:
            print("Opción no válida. Intenta nuevamente.")



#Llamadas a los procedimientos de la base de datos

#clientes:

def agregar_cliente():
    #hay procedimiento
    #nombre:str, email:str, telefono:str

    nombre_cli:str = recibir_input("Ingresa el nombre del cliente: ", "El nombre no puede estar vacío. Intenta nuevamente.", "str")
    
    correo_cli:str = recibir_input("Ingresa el correo electrónico del cliente: ", "El correo no puede estar vacío. Intenta nuevamente.", "str")

    telefono_cli:str = recibir_input("Ingresa el número de teléfono del cliente: ", "El telefono no puede estar vacío. Intenta nuevamente.", "str")

    direccion_cli:str = recibir_input("Ingresa la dirección cliente: ", "La direccion no puede estar vacía. Intenta nuevamente.", "str")

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    try:
        cursor.callproc('RegistrarCliente', (nombre_cli, correo_cli, telefono_cli, direccion_cli))

        conexion.commit()

        cursor.execute("SELECT * FROM Clientes WHERE nombre = %s", (nombre_cli,))
        cliente = cursor.fetchone()

        if cliente:
            print(Fore.GREEN + f"Cliente registrado exitosamente: {cliente}")
        else:
            print(Fore.RED + "El cliente no fue encontrado después de ser registrado.")

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al agregar cliente: {err}")
    finally:

        cursor.close()
        conexion.close()


def actualizar_cliente():

    id_cliente:int = recibir_input("Ingrese el ID del cliente: ", "El ID no puede estar vacio", "int")

    nombre_cli:str = recibir_input("Ingresa el nombre del cliente: ", "El nombre no puede estar vacío. Intenta nuevamente.", "str")
    
    correo_cli:str = recibir_input("Ingresa el correo electrónico del cliente: ", "El correo no puede estar vacío. Intenta nuevamente.", "str")

    telefono_cli:str = recibir_input("Ingresa el número de teléfono del cliente: ", "El telefono no puede estar vacío. Intenta nuevamente.", "str")

    direccion_cli:str = recibir_input("Ingresa la dirección cliente: ", "La direccion no puede estar vacía. Intenta nuevamente.", "str")


    conexion = obtener_conexion()

    cursor = conexion.cursor()

    if id_cliente == 0:
        id_cliente = 1

    try:

        cursor.callproc('ActualizarCliente', (id_cliente, nombre_cli, correo_cli, telefono_cli, direccion_cli))

        conexion.commit()

        cursor.execute("SELECT * FROM Clientes WHERE id_cliente = %s", (id_cliente,))
        cliente = cursor.fetchone()

        if cliente:
            print(Fore.GREEN + f"Cliente editado exitosamente: {cliente}")
        else:
            print(Fore.RED + "El cliente no fue encontrado después de ser editado.")

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al editar cliente: {err}")
    finally:
        cursor.close()
        conexion.close()


def mostrar_clientes():
    conexion = obtener_conexion()
    cursor = cursor = conexion.cursor(buffered=True)


    try:
        cursor.callproc('VerClientes')

        for resultado in cursor.stored_results():
            clientes = resultado.fetchall()

            print(Fore.GREEN + "Clientes:")

            for cliente in clientes:
                print(cliente)

        conexion.commit()
    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al mostrar clientes: {err}")
    finally:
        cursor.close()
        conexion.close()


#productos:

def agregar_producto():

    nombre_prod:str = recibir_input("Ingresa el nombre del producto: ", "El nombre no puede estar vacío. Intenta nuevamente.", "str")
        
    categoria_prod:str = recibir_input("Ingresa el nombre de la categoria del producto: ", "La categoria no puede estar vacía. Intenta nuevamente.", "str")

    precio_prod:float = recibir_input("Ingrese el precio del producto","EL precio no puede estar vacio", "float")
    
    stock_prod:int = recibir_input("Ingrese la cantidad de productos en stock", "el stock no puede estar vacio", "int")
    
    conexion = obtener_conexion()

    cursor = conexion.cursor()

    try:
        cursor.callproc('AgregarProducto', (nombre_prod,categoria_prod,precio_prod,stock_prod))

        conexion.commit()

        cursor.execute("SELECT * FROM Productos WHERE nombre = %s", (nombre_prod,))

        producto = cursor.fetchone()

        if producto:
            print(Fore.GREEN + f"Producto agregado exitosamente: {producto}")
        else:
                print(Fore.RED + "El producto no fue encontrado después de ser agregado.")

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al agregar producto: {err}")
    finally:

        cursor.close()
        conexion.close()

    

def actualizar_producto():
    #parametros, id_producto:int, nuevo_nombre:str, nueva_categoria:str, nuevo_precio:float, nuevo_stock:int 
    id_prod:int = recibir_input("Ingrese el ID del producto: ", "El ID no puede estar vacio.", "int")

    nombre_prod:str = recibir_input("Ingresa el nombre del producto: ", "El nombre no puede estar vacío. Intenta nuevamente.", "str")
        
    categoria_prod:str = recibir_input("Ingresa el nombre de la categoria del producto: ", "La categoria no puede estar vacía. Intenta nuevamente.", "str")

    precio_prod:float = recibir_input("Ingrese el precio del producto","EL precio no puede estar vacio", "float")
    
    stock_prod:int = recibir_input("Ingrese la cantidad de productos en stock", "el stock no puede estar vacio", "int")

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    if id_prod == 0:
        id_prod = 1

    try:

        cursor.callproc('ActualizarProducto', (id_prod, nombre_prod, categoria_prod, precio_prod, stock_prod))

        conexion.commit()

        cursor.execute("SELECT * FROM Productos WHERE nombre = %s", (nombre_prod,))
        producto = cursor.fetchone()

        if producto:
            print(Fore.GREEN + f"Producto actualizado exitosamente: {producto}")
        else:
            print(Fore.RED + "El producto no fue encontrado después de ser actualizado.")

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al actualizar el producto: {err}")
    finally:
        cursor.close()
        conexion.close()



def ver_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(buffered=True)

    try:
        cursor.callproc('VerProductos')

        for resultado in cursor.stored_results():
            productos = resultado.fetchall()

            print(Fore.GREEN + "Producto:")

            for producto in productos:
                print(producto)

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al mostrar productos: {err}")
    finally:
        cursor.close()
        conexion.close()



def eliminar_producto():

    id_prod:int = recibir_input("Ingrese el ID del producto: ", "El ID no puede estar vacio.", "int")

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM Productos WHERE id_producto = %s", (id_prod,))
        result = cursor.fetchone()

        if result[0] > 0:

            cursor.callproc('EliminarProducto', (id_prod,))
            conexion.commit()

            print(Fore.LIGHTYELLOW_EX + f"Producto con ID: {id_prod} eliminado correctamente")
        else:
            print(Fore.RED + f"Producto con ID: {id_prod} no encontrado en la base de datos")

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al eliminar el producto: {err}")
    finally:
        cursor.close()
        conexion.close()
    

#ordenes:

def mostrar_ordenes_por_cliente():
    #parametros, cliente_id:int
    id_cliente:int = recibir_input("Ingrese el ID del cliente: ", "El ID no puede estar vacio", "int")

    if id_cliente == 0:
        id_cliente = 1
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:

        cursor.execute("SELECT COUNT(*) FROM Clientes WHERE id_cliente = %s", (id_cliente,))
        result = cursor.fetchone()

        if result[0] > 0:


            cursor.callproc('MostrarOrdenesPorCliente', (id_cliente,))

            for resultado in cursor.stored_results():
                clientes = resultado.fetchall()

                print(Fore.GREEN + f"Ordenes del cliente con ID {id_cliente}: ")

                for cliente in clientes:
                    print(cliente)
        else:
            print(Fore.RED + f"Cliente con ID: {id_cliente} no encontrado en la base de datos")

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al mostrar la consulta: {err}")
    
    finally:
        cursor.close()
        conexion.close()


def modificar_ordenes_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    id_prod = recibir_input("Ingrese el ID del producto: ", "El ID no puede estar vacío.", "int")
    

    if id_prod == 0:
        id_prod = 1    

    try:
        cursor.execute("SELECT COUNT(*) FROM Productos WHERE id_producto = %s", (id_prod,))
        result = cursor.fetchone()

        if result[0] > 0:

            cant_max = recibir_input("Ingrese la cantidad máxima: ", "La cantidad no puede estar vacía", "int")

            cursor.callproc('ModificarOrdenesProducto', (id_prod, cant_max))
            conexion.commit()
            print(Fore.GREEN + f"Se ha actualizado correctamente el producto con ID {id_prod} a una cantidad máxima de {cant_max}.")
        else:
            print(Fore.RED + f"Producto con ID {id_prod} no encontrado en la base de datos.")

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al modificar la orden del producto: {err}")

    finally:
        cursor.close()
        conexion.close()

    

#busquedas:

def reporte_producto_mas_vendido():

    conexion = obtener_conexion()
    cursor = conexion.cursor(buffered=True)

    try:
        cursor.callproc('ReporteProductoMasVendido')

        for resultado in cursor.stored_results():
            productos = resultado.fetchall()

            print(Fore.GREEN + "Productos mas vendidos:")

            for producto in productos:
                print(producto)
        

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al mostrar el reporte: {err}")
    
    finally:
        cursor.close()
        conexion.close()


def consultar_stock_producto():
    #parametros id_producto:int

    id_prod:int = recibir_input("Ingrese el ID del producto: ", "El ID no puede estar vacio.", "int")

    if id_prod == 0:
        id_prod = 1

    conexion = obtener_conexion()
    cursor = conexion.cursor(buffered=True)

    try:
        cursor.execute("SELECT COUNT(*) FROM Productos WHERE id_producto = %s", (id_prod,))
        result = cursor.fetchone()

        if result[0] > 0:

            cursor.callproc('ConsultarStockProducto', (id_prod,))

            for resultado in cursor.stored_results():
                productos = resultado.fetchall()

                print(Fore.GREEN + f"Stock del producto con ID {id_prod}: ")

                for producto in productos:
                    print(f"Producto: {producto[0]}, Stock disponible: {producto[1]}")
        else:
            print(Fore.RED + f"Producto con ID: {id_prod} no encontrado en la base de datos")

    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al mostrar la consulta: {err}")
    
    finally:
        cursor.close()
        conexion.close()


def clientes_con_mas_ordenes():

    conexion = obtener_conexion()
    cursor = conexion.cursor(buffered=True)

    try:
        cursor.callproc('ClientesConMasOrdenes')

        for resultado in cursor.stored_results():
            clientes = resultado.fetchall()

            print(Fore.GREEN + f"Clientes con mas ordenes: ")

            for cliente in clientes:
                print(cliente)
        
    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al mostrar la consulta: {err}")
    finally:
        cursor.close()
        conexion.close()

    

#sql

def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='utntup',   
        database='sistema_ventas' 
    )


#helpers functions

def recibir_input(msg:str, err_msg:str, type:str):

    while True:

        variable:str = input(msg)

        if not variable.strip():
            print(err_msg)
        else:
            break 

    
    if type == "int":
        try:

            return abs(int(variable))
        
        except ValueError:
            print("ingrese un numero entero.")
            return recibir_input(msg, err_msg, type)
    
    elif type == "float":
        try:

            return abs(float(variable))
        
        except ValueError:
            print("ingrese un numero decimal.")
            return recibir_input(msg, err_msg, type)

    return variable


if __name__ == "__main__":
    init(autoreset=True)
    menu_principal()

from procedures.clients import mostrar_clientes, agregar_cliente, actualizar_cliente, eliminar_cliente
from procedures.products import mostrar_productos, agregar_producto, actualizar_producto, eliminar_producto
from procedures.orders import mostrar_ordenes_por_cliente, reporte_producto_mas_vendido, clientes_con_mas_ordenes

def menu_principal():
    while True:
        print("Bienvenido a la Aplicación de Procedimientos SQL")
        print("1. Gestionar Productos")
        print("2. Gestionar Clientes")
        print("3. Procesar Órdenes")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            gestionar_productos()
        elif opcion == '2':
            gestionar_clientes()
        elif opcion == '3':
            procesar_ordenes()
        elif opcion == '4':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def gestionar_productos():
    while True:
        print("Gestión de Productos")
        print("1. Mostrar todos los productos")
        print("2. Registrar nuevo producto")
        print("3. Actualizar información de un producto")
        print("4. Eliminar producto")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción (0-4): ")

        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def gestionar_clientes():
    while True:
        print("Gestión de Clientes")
        print("1. Mostrar todos los clientes")
        print("2. Registrar nuevo cliente")
        print("3. Actualizar información de un cliente")
        print("4. Eliminar cliente")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción (0-4): ")

        if opcion == '1':
            mostrar_clientes()
        elif opcion == '2':
            agregar_cliente()
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def procesar_ordenes():
    while True:
        print("Procesamiento de Órdenes")
        print("1. Mostrar órdenes por cliente")
        print("2. Reporte de producto más vendido")
        print("3. Clientes con más órdenes")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción (0-4): ")

        if opcion == '1':
            mostrar_ordenes_por_cliente()
        elif opcion == '2':
            reporte_producto_mas_vendido()
        elif opcion == '3':
            clientes_con_mas_ordenes()
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()
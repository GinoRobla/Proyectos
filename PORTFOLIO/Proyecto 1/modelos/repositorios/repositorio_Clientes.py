from modelos.entidades.cliente import Cliente 
import json

class RepositorioClientes:
    ruta_archivo = r"C:\Proyectos\PORTFOLIO\Proyecto 1\datos\clientes.json"

    def __init__(self):
        self.__clientes = []
        self.__cargarClientes()

    def __cargarClientes(self):
        try:
            with open(RepositorioClientes.ruta_archivo, "r") as archivo:
                lista_dicc_clientes = json.load(archivo)
                for cliente in lista_dicc_clientes:
                    self.__clientes.append(Cliente.fromDiccionario(cliente))
        except FileNotFoundError:
            print("No se encontró el archivo de clientes")
        except Exception as e:
            print("Error cargando los clientes del archivo.\n" + str(e))

    def __guardarClientes(self):
        try:
            with open(RepositorioClientes.ruta_archivo, "w") as archivo:
                lista_dicc_clientes = [cliente.toDiccionario() for cliente in self.__clientes]
                json.dump(lista_dicc_clientes, archivo, indent=4)
        except Exception as e:
            print("Error guardando los clientes en el archivo.\n" + str(e))
    
    def obtenerClientes(self):
        return self.__clientes
    
    def obtenerClientePorDni(self, dni: int) -> Cliente:
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El DNI debe ser un número entero positivo.")
        
        for cliente in self.__clientes:
            if cliente.obtenerDni() == dni:
                return cliente
        return None
    
    def existeCliente(self, dni: int) -> bool:
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El DNI debe ser un número entero positivo.")
        
        for cliente in self.__clientes:
            if cliente.obtenerDni() == dni:
                return True
        return False

    def agregarCliente(self, cliente: Cliente) -> None:
        if not isinstance(cliente, Cliente):
            raise ValueError("El objeto debe ser una instancia de Cliente")
        
        if self.existeCliente(cliente.obtenerDni()):
            raise ValueError("Ya existe un cliente con ese DNI")
        
        self.__clientes.append(cliente)
        self.__guardarClientes()

    def actualizarCliente(self, dni: int, cliente: Cliente) -> bool:
        if not isinstance(cliente, Cliente):
            raise ValueError("El objeto debe ser una instancia de Cliente")
        
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El DNI debe ser un número entero positivo.")
        
        for cliente_a_modificar in self.__clientes:
            if cliente_a_modificar.obtenerDni() == dni:
                self.__clientes.remove(cliente_a_modificar)
                self.__clientes.append(cliente)
                self.__guardarClientes()
                return True
        return False

    def eliminarCliente(self, dni: int) -> bool:
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El DNI debe ser un número entero positivo.")
        
        for cliente in self.__clientes:
            if cliente.obtenerDni() == dni:
                self.__clientes.remove(cliente)
                self.__guardarClientes()
                return True
        return False

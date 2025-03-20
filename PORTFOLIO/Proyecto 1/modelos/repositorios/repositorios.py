from modelos.repositorios.repositorio_Bebidas import RepositorioBebidas
from modelos.repositorios.repositorio_Clientes import RepositorioClientes

bebidas = None
clientes = None

def obtenerRepoBebidas():
    global bebidas
    if bebidas == None:
        bebidas = RepositorioBebidas()
    return bebidas

def obtenerRepoClientes():
    global clientes
    if clientes == None:
        clientes = RepositorioClientes()
    return clientes
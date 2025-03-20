from modelos.repositorios.repositorio_Bebidas import RepositorioBebidas

bebidas = None

def obtenerRepoBebidas():
    global bebidas
    if bebidas == None:
        bebidas = RepositorioBebidas()
    return bebidas
from abc import ABC, abstractmethod

class Bebida(ABC):

    def __init__(self, nombre:str, costo:float, stock:int, mililitros:int):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise Exception("El nombre debe ser un string")
        if not isinstance(costo, (int, float)) or costo < 0:
            raise Exception("El costo debe ser un número positivo")
        if not isinstance(stock, int) or stock < 0:
            raise Exception("El stock debe ser un número positivo")
        if not isinstance(mililitros, int) or mililitros < 0:
            raise ValueError("Los mililitros del envase deben ser un número positivo")
        self._nombre = nombre
        self._costo = costo
        self._stock = stock
        self._mililitros = mililitros

    @abstractmethod
    def obtenerPrecio(self):
        pass

    def obtenerNombre(self):
        return self._nombre
    
    def obtenerCosto(self):
        return self._costo
    
    def obtenerStock(self):
        return self._stock
    
    def obtenerMililitros(self):
        return self._mililitros
    
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        self._nombre = nombre

    def establecerCosto(self, costo:float):
        if not isinstance(costo, (int, float)) or costo < 0:
            raise ValueError("El costo debe ser un número positivo")
        self._costo = costo

    def establecerMililitros(self, mililitros:int):
        if not isinstance(mililitros, int, (float)) or mililitros < 0: #agregue para que valide si no es float tambien porque los mililitros pueden ser decimales tambien.
            raise ValueError("Los mililitros del envase deben ser un número positivo")
        self._mililitros = mililitros
    
    def actualizarStock(self, cantidad:int, costo_reposicion:float):
        """Incrementa el stock de la bebida en la cantidad indicada y actualiza el costo de reposición"""
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo")
        if not isinstance(costo_reposicion, (int, float)) or costo_reposicion < 0:
            raise ValueError("El costo de reposición debe ser un número positivo")
        self._stock += cantidad
        self._costo = costo_reposicion
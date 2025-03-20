from modelos.entidades.bebida import Bebida

class BebidaSinAlcohol(Bebida):
    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        return cls(diccionario["nombre"], diccionario["costo"], diccionario["stock"], diccionario["mililitros"], diccionario["sabor"], diccionario["natural"])

    def __init__(self, nombre:str, costo:float, stock:int, mililitros:int, sabor: str, natural: bool):
        super().__init__(nombre, costo, stock, mililitros)
        if not isinstance(sabor, str) or not sabor.strip():
            raise ValueError("El sabor debe ser un string y no puede estar vacío")
        if not isinstance(natural, bool):
            raise ValueError("El atributo natural debe ser booleano")
        self.__sabor = sabor
        self.__natural = natural
    
    
    def obtenerSabor(self):
        return self.__sabor
    
    def obtenerNatural(self):
        return self.__natural
    
    def establecerSabor(self, sabor:str):
        if not isinstance(sabor, str) or sabor == "":
            raise ValueError("El sabor no puede ser vacío")
        self.__sabor = sabor
    
    def establecerNatural(self, natural:bool):
        if not isinstance(natural, bool):
            raise ValueError("El atributo natural debe ser booleano")
        self.__natural = natural

    def obtenerPrecio(self):
        return self._costo * 1.5
    
        
    def toDiccionario(self):
        return {
            "nombre": self._nombre,
            "costo": self._costo,
            "stock": self._stock,
            "mililitros": self._mililitros,
            "sabor": self.__sabor,
            "natural": self.__natural,
            "precio": self.obtenerPrecio()
        }
from modelos.entidades.bebida import Bebida

class BebidaConAlcohol(Bebida):
    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        return cls(diccionario["nombre"], diccionario["costo"], diccionario["stock"], diccionario["mililitros"], diccionario["graduacionAlcoholica"])

    def __init__(self, nombre:str, costo:float, stock:int, mililitros:int, graduacionAlcoholica: float):
        super().__init__(nombre, costo, stock, mililitros)
        if not isinstance(graduacionAlcoholica, (int, float)) or graduacionAlcoholica < 0 or graduacionAlcoholica > 100:
            raise ValueError("La graduación alcohólica debe ser un número positivo")
        self.__graduacionAlcoholica = graduacionAlcoholica

    def obtenerPrecio(self):
        return self._costo * 1.6
    
    def obtenerGraduacionAlcoholica(self):
        return self.__graduacionAlcoholica
    
    def establecerGraduacionAlcoholica(self, graduacionAlcoholica:float):
        if not isinstance(graduacionAlcoholica, (int, float)) or graduacionAlcoholica < 0 or graduacionAlcoholica > 100:
            raise ValueError("La graduación alcohólica debe ser un número positivo")
        self.__graduacionAlcoholica = graduacionAlcoholica

    def toDiccionario(self):
        return {
            "nombre": self._nombre,
            "costo": self._costo,
            "stock": self._stock,
            "mililitros": self._mililitros,
            "graduacionAlcoholica": self.__graduacionAlcoholica,
            "precio": self.obtenerPrecio()
        }
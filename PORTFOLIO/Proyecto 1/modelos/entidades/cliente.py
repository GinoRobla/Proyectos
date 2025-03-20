from modelos.entidades.bebida import Bebida

class Cliente:
    #atributos de clase
    
    #metodo de clase
    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        return cls(diccionario["dni"], diccionario["nombre"], diccionario["apellido"], diccionario["bebidaFavorita"])
    def __init__(self,dni:int, nombre: str, apellido: str, bebidaFavorita:str):#constructor
        #validaciones
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un número entero")
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser un string")
        if not isinstance(bebidaFavorita, Bebida):
            raise ValueError("La bebida favorita debe ser una instancia de la clase Bebida")
        #atributos de instancia
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__bebidaFavorita = bebidaFavorita
    #consultas
    def obtenerDni(self):
        return self.__dni
    def obtenerNombre(self):
        return self.__nombre
    def obtenerApellido(self):
        return self.__apellido
    def obtenerBebidaFavorita(self):
        return self.__bebidaFavorita
    #comandos
    def establecerDni(self, dni:int):
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un número entero")
        self.__dni = dni
    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        self.__nombre = nombre
    def establecerApellido(self, apellido: str):
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser un string")
        self.__apellido = apellido
    def establecerBebidaFavorita(self, bebidaFavorita: Bebida):
        if not isinstance(bebidaFavorita, Bebida):
            raise ValueError("La bebida favorita debe ser una instancia de la clase Bebida")
        self.__bebidaFavorita = bebidaFavorita
    def toDiccionario(self):
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "bebidaFavorita": self.__bebidaFavorita.toDiccionario()
        }
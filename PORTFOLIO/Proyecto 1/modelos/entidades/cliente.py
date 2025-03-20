from modelos.entidades.bebida import Bebida
from modelos.entidades.bebidaSinAlcohol import BebidaSinAlcohol
from modelos.entidades.bebidaConAlcohol import BebidaConAlcohol

class Cliente:
    @classmethod
    def fromDiccionario(cls, diccionario: dict):
        bebida_favorita = None
        if "graduacionAlcoholica" in diccionario["bebidaFavorita"]:
            bebida_favorita = BebidaConAlcohol.fromDiccionario(diccionario["bebidaFavorita"])
        else:
            bebida_favorita = BebidaSinAlcohol.fromDiccionario(diccionario["bebidaFavorita"])
        return cls(diccionario["dni"], diccionario["nombre"], diccionario["apellido"], bebida_favorita)

    def __init__(self, dni: int, nombre: str, apellido: str, bebidaFavorita: Bebida):
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un número entero")
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser un string")
        if not isinstance(bebidaFavorita, Bebida):
            raise ValueError("La bebida favorita debe ser una instancia de la clase Bebida")
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__bebidaFavorita = bebidaFavorita

    def obtenerDni(self):
        return self.__dni

    def obtenerNombre(self):
        return self.__nombre

    def obtenerApellido(self):
        return self.__apellido

    def obtenerBebidaFavorita(self):
        return self.__bebidaFavorita

    def toDiccionario(self):
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "bebidaFavorita": self.__bebidaFavorita.toDiccionario()
        }
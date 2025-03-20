from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoBebidas
from modelos.entidades.bebida import Bebida
from modelos.entidades.bebidaConAlcohol import BebidaConAlcohol 
from modelos.entidades.bebidaSinAlcohol import BebidaSinAlcohol

repo_bebidas = obtenerRepoBebidas()

bp_bebidas = Blueprint("bp_bebidas", __name__)

@bp_bebidas.route("/bebidas", methods = ["GET"])
def listar_bebidas():
    return jsonify([bebida.toDiccionario() for bebida in repo_bebidas.obtenerBebidas()]), 200 #agregamos el codigo de respuesta 200 

@bp_bebidas.route("/bebidas/<string:nombre>", methods = ["GET"])
def obtener_bebida(nombre):
    bebida = repo_bebidas.obtenerBebidaPorNombre(nombre)
    if bebida == None:
        return jsonify({"error": "Bebida no encontrada"}), 404
    return jsonify(bebida.toDiccionario()), 200 #agregamos el codigo de respuesta 200 

@bp_bebidas.route("/bebidas", methods=["POST"])  
def agregar_bebida():
    if request.is_json:  # valida que los datos sean de tipo JSON
        datos = request.json
        if "nombre" in datos and "stock" in datos and "costo" in datos:  # valida que los campos obligatorios lleguen en el JSON
            if "graduacionAlcoholica" in datos:
                bebida = BebidaConAlcohol.fromDiccionario(datos)
                tipo = "con alcohol"  
            else:
                bebida = BebidaSinAlcohol.fromDiccionario(datos)  
                tipo = "sin alcohol" 
            if repo_bebidas.existeBebida(datos["nombre"]):  # valida si ya existe una bebida con ese nombre
                respuesta = {"error": "Ya existe una bebida con el nombre especificado."}  
                codigoRespuesta = 400  # agregamos la variable codigo de respuesta así no nos quedan tantos returns
            else:
                repo_bebidas.agregarBebida(bebida) 
                respuesta = {  
                    "Mensaje": f"Bebida {tipo} agregada con éxito.",
                    "bebida": bebida.toDiccionario()
                }
                codigoRespuesta = 201  
        else:
            respuesta = {"error": "Faltan datos en el JSON. Debe incluir 'nombre', 'stock' y 'costo'."}
            codigoRespuesta = 400  
    else:
        respuesta = {"error": "Los datos deben estar en formato JSON."}
        codigoRespuesta = 400 
    return jsonify(respuesta), codigoRespuesta

@bp_bebidas.route("/bebidas/<string:nombre>", methods=["PUT"])  
def modificar_bebida(nombre):
    if request.is_json:  #valida que los datos sea de tipo json
        datos = request.json  
        if "nombre" in datos and "stock" in datos and "costo" in datos: #agrego que valide que los campos obligatorios lleguen en el json
            if "graduacionAlcoholica" in datos:  
                bebida = BebidaConAlcohol.fromDiccionario(datos)  
                tipo = "con alcohol"  
            else:
                bebida = BebidaSinAlcohol.fromDiccionario(datos)  
                tipo = "sin alcohol" 
            if repo_bebidas.existeBebida(nombre): #valida si ya existe una bebida con ese nombre para asi modificarla
                if repo_bebidas.actualizarBebida(nombre, bebida):  
                    respuesta = {  
                        "Mensaje": f"Bebida {tipo} actualizada con éxito.",
                        "bebida": bebida.toDiccionario()
                    }
                    codigoRespuesta = 200  #agregamos la variable codigo de respuesta asi no nos quedan tantos returns
                else:
                    respuesta = {"error": "No se encontró la bebida a actualizar"} 
                    codigoRespuesta = 404  
            else:
                respuesta = {"error": "No se encontró la bebida a actualizar"} 
        else:
            respuesta = {"error": "Faltan datos en el JSON. Debe incluir 'nombre', 'stock' y 'costo'."} 
            codigoRespuesta = 400  
    else:
        respuesta = {"error": "Los datos deben estar en formato JSON."}  
        codigoRespuesta = 400  
    return jsonify(respuesta), codigoRespuesta  

@bp_bebidas.route("/bebidas/<string:nombre>", methods = ["DELETE"])
def eliminar_bebida(nombre):
    if repo_bebidas.existeBebida(nombre): #valido si existe antes de eliminarla
        repo_bebidas.eliminarBebida(nombre)
        return jsonify({"Mensaje":f"Bebida eliminada con éxito."}), 200 #agregamos codigo de respuesta
    return jsonify({"error": "No se encontró la bebida a eliminar"}), 404

@bp_bebidas.route("/bebidas/<string:nombre>/precio", methods=["GET"])
def obtener_precio_bebida(nombre):
    bebida = repo_bebidas.obtenerBebidaPorNombre(nombre)
    if bebida is None:
        return jsonify({"error": "Bebida no encontrada"}), 404
    return jsonify({"nombre": bebida.obtenerNombre(), "precio": bebida.obtenerPrecio()}), 200 #agregamos codigo de respuesta
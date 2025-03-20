from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoClientes
from modelos.entidades.cliente import Cliente

repo_clientes = obtenerRepoClientes()

bp_clientes = Blueprint("bp_clientes", __name__)

@bp_clientes.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify([cliente.toDiccionario() for cliente in repo_clientes.obtenerClientes()]), 200  

@bp_clientes.route("/clientes/<int:dni>", methods=["GET"])
def obtener_cliente(dni):
    cliente = repo_clientes.obtenerClientePorDni(dni)
    if cliente is None:
        return jsonify({"error": "Cliente no encontrado"}), 404
    return jsonify(cliente.toDiccionario()), 200  

@bp_clientes.route("/clientes", methods=["POST"])
def agregar_cliente():
    if request.is_json:  
        datos = request.json
        if "dni" in datos and "nombre" in datos and "apellido" in datos and "bebidaFavorita" in datos:
            try:
                cliente = Cliente.fromDiccionario(datos)
                if repo_clientes.existeCliente(cliente.obtenerDni()):
                    respuesta = {"error": "Ya existe un cliente con ese DNI"}
                    codigoRespuesta = 400  
                else:
                    repo_clientes.agregarCliente(cliente)  
                    respuesta = {
                        "Mensaje": "Cliente agregado con éxito",
                        "cliente": cliente.toDiccionario()
                    }
                    codigoRespuesta = 201  
            except ValueError as e:
                respuesta = {"error": str(e)}
                codigoRespuesta = 400  
        else:
            respuesta = {"error": "Faltan datos en el JSON. Debe incluir 'dni', 'nombre', 'apellido' y 'bebidaFavorita'."}
            codigoRespuesta = 400
    else:
        respuesta = {"error": "Los datos deben estar en formato JSON."}
        codigoRespuesta = 400  
    return jsonify(respuesta), codigoRespuesta  

@bp_clientes.route("/clientes/<int:dni>", methods=["PUT"])
def modificar_cliente(dni):
    if request.is_json:  
        datos = request.json
        if "dni" in datos and "nombre" in datos and "apellido" in datos and "bebidaFavorita" in datos:
            try:
                cliente = Cliente.fromDiccionario(datos)
                if repo_clientes.actualizarCliente(dni, cliente):
                    respuesta = {
                        "Mensaje": "Cliente actualizado con éxito",
                        "cliente": cliente.toDiccionario()
                    }
                    codigoRespuesta = 200  
                else:
                    respuesta = {"error": "No se encontró el cliente a actualizar"}
                    codigoRespuesta = 404  
            except ValueError as e:
                respuesta = {"error": str(e)}
                codigoRespuesta = 400  
        else:
            respuesta = {"error": "Faltan datos en el JSON. Debe incluir 'dni', 'nombre', 'apellido' y 'bebidaFavorita'."}
            codigoRespuesta = 400
    else:
        respuesta = {"error": "Los datos deben estar en formato JSON."}
        codigoRespuesta = 400  
    return jsonify(respuesta), codigoRespuesta  

@bp_clientes.route("/clientes/<int:dni>", methods=["DELETE"])
def eliminar_cliente(dni):
    if repo_clientes.eliminarCliente(dni):
        return jsonify({"Mensaje": "Cliente eliminado con éxito"}), 200  
    return jsonify({"error": "No se encontró el cliente a eliminar"}), 404  

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config

class IphoneAPI:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.conexion = MySQL(self.app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/iphones', methods=['GET'])(self.leer_iphones)
        self.app.route('/iphones/<IMEI>', methods=['GET'])(self.buscar_iphones)
        self.app.route('/iphones', methods=['POST'])(self.agregar_iphone)
        self.app.route('/iphones/<IMEI>', methods=['PUT'])(self.modificar_iphone)
        self.app.route('/iphones/<IMEI>', methods=['DELETE'])(self.eliminar_iphone)

    def leer_iphones(self):
        try:
            cursor = self.conexion.connection.cursor()
            sql = "SELECT IMEI, modelo, color, gb, bateria, precio FROM iphone"
            cursor.execute(sql)
            datos = cursor.fetchall()
            iphones = []
            for fila in datos:
                iphone = {
                    'IMEI': fila[0],
                    'modelo': fila[1],
                    'color': fila[2],
                    'gb': fila[3],
                    'bateria': fila[4],
                    'precio': fila[5]
                }
                iphones.append(iphone)
            return jsonify({'iPhones': iphones, 'nota': "iPhones en stock."})
        except Exception as e:
            return jsonify({'error tipo': str(e)})

    def buscar_iphones(self, IMEI):
        try:
            cursor = self.conexion.connection.cursor()
            sql = f"SELECT IMEI, modelo, color, gb, bateria, precio FROM iphone WHERE IMEI = '{IMEI}'"
            cursor.execute(sql)
            datos = cursor.fetchone()
            if datos:
                iphone = {
                    'IMEI': datos[0],
                    'modelo': datos[1],
                    'color': datos[2],
                    'gb': datos[3],
                    'bateria': datos[4],
                    'precio': datos[5]
                }
                return jsonify({'iphone': iphone, 'mensaje': 'iPhone encontrado'})
            else:
                return jsonify({'mensaje': 'iPhone no encontrado'})
        except Exception as e:
            return jsonify({'error tipo': str(e)})

    def agregar_iphone(self):
        try:
            cursor = self.conexion.connection.cursor()
            sql = """INSERT INTO iphone (IMEI, modelo, color, gb, bateria, precio) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                request.json['IMEI'], 
                request.json['modelo'], 
                request.json['color'], 
                request.json['gb'], 
                request.json['bateria'], 
                request.json['precio']
            ))
            self.conexion.connection.commit()
            return jsonify({'mensaje': "iPhone Registrado"})
        except Exception as e:
            return jsonify({'error tipo': str(e)})

    def modificar_iphone(self, IMEI):
        try:
            cursor = self.conexion.connection.cursor()
            sql = "UPDATE iphone SET bateria = %s, precio = %s WHERE IMEI = %s"
            cursor.execute(sql, (request.json['bateria'], request.json['precio'], IMEI))
            self.conexion.connection.commit()
            return jsonify({'mensaje': "iPhone actualizado"})
        except Exception as e:
            return jsonify({'error tipo': str(e)})

    def eliminar_iphone(self, IMEI):
        try:
            cursor = self.conexion.connection.cursor()
            sql = f"DELETE FROM iphone WHERE IMEI = '{IMEI}'"
            cursor.execute(sql)
            self.conexion.connection.commit()
            return jsonify({'mensaje': "iPhone Eliminado"})
        except Exception as e:
            return jsonify({'error tipo': str(e)})

if __name__ == '__main__':
    api = IphoneAPI()
    api.app.config.from_object(config['development'])
    api.app.run(debug=True)

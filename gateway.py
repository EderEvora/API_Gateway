from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

USER_SERVICE  = 'http://localhost:5001'
ORDER_SERVICE   = 'http://localhost:5003'

# 2 INSTANCE pro load balancer
PRODUCT_INSTANCE = ['http://localhost:5002', 'http://localhost:5004']
indice_product = 0


def next_instance_product():
    global indice_product
    instancia = PRODUCT_INSTANCE[indice_product]
    indice_product = (indice_product + 1) % len(PRODUCT_INSTANCE)
    return instancia


# USERS ZONE --------------
@app.route('/users', methods=['GET'])
def get_users():
    resposta = requests.get(f"{USER_SERVICE}/users")
    return jsonify(resposta.json())

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    resposta = requests.get(f"{USER_SERVICE}/users/{id}")
    return jsonify(resposta.json())


# PRODUCTS ZONE ------------
@app.route('/products', methods=['GET'])
def get_products():
    destino = next_instance_product()
    print(f"[GATEWAY] /products → {destino}")
    resposta = requests.get(f"{destino}/products")
    return jsonify(resposta.json())

@app.route('/products/<int:id>', methods=['PUT'])
def edit_product(id):
    destino = next_instance_product()
    resposta = requests.put(f"{destino}/products/{id}", json=request.get_json())
    return jsonify(resposta.json())


# ORDERS ZONE ---------------
@app.route('/orders', methods=['GET'])
def get_orders():
    resposta = requests.get(f"{ORDER_SERVICE}/orders")
    return jsonify(resposta.json())

app.run(port=5000, host='localhost', debug=True)
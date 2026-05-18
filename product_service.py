from flask import Flask, jsonify, request
import sys

app = Flask(__name__)

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5002
INSTANCE = f"product-service:{PORT}"

products = [ 
    {'id': 1, 'name': 'Laptop', 'brand': 'Huawei', 'price': 30000}, 
    {'id': 2, 'name': 'Mouse', 'brand': 'Mitsai', 'price': 1500}, 
    {'id': 3, 'name': 'Telemovel', 'brand': 'Xiaomi Redmi', 'price': 18000} 
]

@app.route('/products', methods=['GET'])
def get_products():
    print(f"[{INSTANCE}] GET /products")
    return jsonify({'instance': INSTANCE, 'data': products})

@app.route('/products/<int:id>', methods=['PUT'])
def edit_product(id):
    data = request.get_json()
    for indice, product in enumerate(products):
        if product['id'] == id:
            products[indice].update(data)
            return jsonify({'instance': INSTANCE, 'data': products[indice]})


app.run(port=PORT, host='localhost', debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

products = [ 
    {'id': 1, 'name': 'Laptop', 'brand': 'Huawei', 'price': 30000}, 
    {'id': 2, 'name': 'Mouse', 'brand': 'Mitsai', 'price': 1500}, 
    {'id': 3, 'name': 'Telemovel', 'brand': 'Xiaomi Redmi', 'price': 18000} 
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=['PUT'])
def edit_product(id):
    data = request.get_json()
    for indice, product in enumerate(products):
        if product['id'] == id:
            products[indice].update(data)
            return jsonify(products[indice])


app.run(port=5002, debug=True)
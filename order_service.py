from flask import Flask, jsonify
import requests

app = Flask(__name__)

orders = [
    {
        'id': 1,
        'user_id': 1,
        'products': [1, 2], 
        'total': 31500
    },
    {
        'id': 2,
        'user_id': 2,
        'products': [3], 
        'total': 18000
    }
]

@app.route('/orders', methods=['GET'])
def get_orders():
    users = requests.get('http://localhost:5001/users').json()
    products = requests.get('http://localhost:5002/products').json()

    return jsonify({
        'orders': orders,
        'users': users,
        'products': products
    })


app.run(port=5003, debug=True)
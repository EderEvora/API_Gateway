from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/users')
def users():
    return jsonify(requests.get('http://localhost:5001/users').json())

@app.route('/products')
def products():
    return jsonify(requests.get('http://localhost:5002/products').json())

@app.route('/orders')
def orders():
    return jsonify(requests.get('http://localhost:5003/orders').json())

app.run(port=5000, debug=True)
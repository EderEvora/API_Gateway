from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'Eder Evora'},
    {'id': 2, 'name': 'Luis Ramos'}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    for user in users:
        if user['id'] == id:
            return jsonify(user)

@app.route('/users', methods= ['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(users)

app.run(port=5001, debug=True)
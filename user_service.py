from flask import Flask, jsonify

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


app.run(port=5001, debug=True)
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Data user statis
users = {
    "1": {"id": "1", "name": "Alice"},
    "2": {"id": "2", "name": "Bob"}
}

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

#UserService sebagai consumer: ambil histori pinjaman dari BookService
@app.route('/users/<user_id>/loans', methods=['GET'])
def get_user_loans(user_id):
    try:
        response = requests.get(f'http://localhost:5001/loans/user/{user_id}')
        return jsonify(response.json()), response.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "BookService tidak tersedia"}), 500

if __name__ == '__main__':
    app.run(port=5000)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Service is running!"})

with app.test_request_context():
    print("Available endpoints:")
    print(app.url_map)

if __name__ == '__main__':
    app.run(port=5001)  



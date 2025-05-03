from flask import Blueprint, request, jsonify
import requests

loans_bp = Blueprint('loans', __name__)

loans = []

@loans_bp.route('/loans', methods=['POST'])
def create_loan():
    data = request.get_json()
    user_id = data.get("user_id")
    book_id = data.get("book_id")

    # Ambil data user dari UserService
    user_response = requests.get(f"http://localhost:5000/users/{user_id}")
    if user_response.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    loan = {"user_id": user_id, "book_id": book_id}
    loans.append(loan)
    return jsonify(loan), 201

@loans_bp.route('/loans/user/<user_id>', methods=['GET'])
def get_loans_by_user(user_id):
    user_loans = [l for l in loans if l["user_id"] == user_id]
    return jsonify(user_loans), 200

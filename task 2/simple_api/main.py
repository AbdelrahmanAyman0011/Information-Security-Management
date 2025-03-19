from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (Replace with a database in production)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask User API!", 200

# GET: Retrieve user by ID
@app.route("/get-user/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404

# POST: Add a new user
@app.route("/add-user", methods=["POST"])
def add_user():
    data = request.json
    user_id = str(data.get("user_id"))
    
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[user_id] = {
        "user_id": user_id,
        "name": data.get("name", "Unknown"),
        "extra": data.get("extra", "")
    }
    return jsonify({"message": "User added successfully"}), 201

# PUT: Update user information
@app.route("/update-user/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    users[user_id].update({
        "name": data.get("name", users[user_id]["name"]),
        "extra": data.get("extra", users[user_id].get("extra", ""))
    })
    return jsonify({"message": "User updated successfully"}), 200

# DELETE: Remove a user
@app.route("/delete-user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)

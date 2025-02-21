from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    user = {"id": len(users) + 1, "name": data['name']}
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

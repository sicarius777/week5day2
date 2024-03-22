from flask import Flask, jsonify, request

app = Flask(__name__)

# sample data
users = [
    {"id": 1, "username": "admin", "password": "admin"},
    {"id": 2, "username": "user", "password": "password"}
]

ships = []

# Routes-user-CRUD-ops

# Read operation - Get all users.
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# check ID weed out rebels.
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'You are rebel scum access denied, deploying assasin droids please stay where you are!'}), 404

# Add a new user to the glorius empire.
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

# Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user.update(request.json)
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 200

# Routes for ship CRUD operations

# Get all ships
@app.route('/ships', methods=['GET'])
def get_ships():
    return jsonify(ships)

# Get a specific ship by ID
@app.route('/ships/<int:ship_id>', methods=['GET'])
def get_ship(ship_id):
    ship = next((ship for ship in ships if ship['id'] == ship_id), None)
    if ship:
        return jsonify(ship)
    else:
        return jsonify({'error': 'Ship lost in the void'}), 404

# Add a new ship
@app.route('/ships', methods=['POST'])
def add_ship():
    new_ship = request.json
    new_ship['id'] = len(ships) + 1
    ships.append(new_ship)
    return jsonify(new_ship), 201

# Update existing ship
@app.route('/ships/<int:ship_id>', methods=['PUT'])
def update_ship(ship_id):
    ship = next((ship for ship in ships if ship['id'] == ship_id), None)
    if ship:
        ship.update(request.json)
        return jsonify(ship)
    else:
        return jsonify({'error': 'ship does not exist hold position for body scan check'}), 404

# Delete a ship
@app.route('/ships/<int:ship_id>', methods=['DELETE'])
def delete_ship(ship_id):
    global ships
    ships = [ship for ship in ships if ship['id'] != ship_id]
    return jsonify({'message': 'Ship destroyed'}), 200

if __name__ == '__main__':
    app.run(debug=True)

# this is kewl. NO REBELS DETECTED

#Im pretty sure i already did what this assighnment is asking by 
    # creating 2 resources one on users and the other on ships unless im wrong
    # let me know and ill add more, could do weapons next.....

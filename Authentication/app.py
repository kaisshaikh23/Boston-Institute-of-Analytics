from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configure the application with a secret key for encoding and decoding JWTs
app.config['JWT_SECRET_KEY'] = 'boston-institute-9876543210'
jwt = JWTManager(app)

# Sample user data for authentication (you should replace this with your own user authentication logic)
users = {
    'user1': {'password': 'boston@123'},
    'user2': {'password': 'institute@321'}
}

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username and password are correct (you should replace this with your own user authentication logic)
    if username in users and password == users[username]['password']:
        # Create an access token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401

# Protected endpoint that requires a valid access token
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)

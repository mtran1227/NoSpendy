import json
import csv
import os
#Install
!pip install flask
!pip install pymongo

#Profile Setup Route-------------------------------------------------------------
app = Flask(__name__)

# Connect to MongoDB (update with your MongoDB URI)
client = MongoClient("mongodb://localhost:27017/")
db = client["user_profiles"]
collection = db["profiles"]

@app.route('/profile', methods=['POST'])
def setup_profile():
    data = request.get_json()

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    password = data.get('password')
    state = data.get('state')
    email = data.get('email')

    if not all([first_name, last_name, username, password, state, email]):
        return jsonify({"error": "All fields are required!"}), 400

    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "state": state,
        "email": email
    }

    result = users_collection.insert_one(user_data)

    return jsonify({
        "message": "Profile created successfully!",
        "user_id": str(result.inserted_id)
    }), 201

#Get Profile Route
@app.route('/profile/<user_id>', methods=['GET'])
def get_profile(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if not user:
        return jsonify({"error": "User not found"}), 404

    user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return jsonify(user), 200



from flask import Flask, jsonify, request

app = Flask(__name__)

# Static Data
users = [
    {"id": 1, "name": "Avi", "age": 30},
    {"id": 2, "name": "Dana", "age": 40},
    {"id": 3, "name": "Rom", "age": 50},
]

# Get ALL users [GET]
# http://localhost:8000/users
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(users)


# Get user By Id [GET]
# # http://localhost:8000/users/5
@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user_filter = list(filter(lambda user: user["id"] == id,users))
    if len(user_filter) == 0:
        return jsonify({"error": "User not found!"})
    return jsonify(user_filter[0])


# create user [POST]
# /users
@app.route("/users", methods=["POST"])
def add_user():
    # request.json => request body from client
    data = request.json
    print(data)
    users.append(data)
    return jsonify("Created")


# Update user [PUT]
# /users/1
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    # request.json => request body from client
    data = request.json
    for user in users:
        if user["id"] == id:
            user["name"] = data["name"]
            user["age"] = data["age"]
            break
    return jsonify("Updated")


# Delete User [DELETE]
# /users/1
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    # 1
    index = -1
    for i in range(len(users)):
        if users[i]["id"] == id:
            index = i
            break
    users.pop(index)
    return jsonify("Deleted")

app.run(port=8000)

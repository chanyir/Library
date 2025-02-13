
from flask import Flask, jsonify, request

cars=[{"id":1, "model":"mazda","year":2020,"driver":{"FirstName":"Avi","LastName":"Cohen"}},
      {"id":2,"model":"bmw","year":2018,"driver":{"FirstName":"Dana","LastName":"Levi"}}]

app=Flask(__name__)


# get
@app.route("/cars",methods=["GET"])
def get_all():
    return jsonify(cars)
# post
@app.route("/cars",methods=["POST"])
def add_car():
    new_car=request.json
    cars.append(new_car)
    return jsonify(cars)

# put
@app.route("/cars/<int:id>",methods=["PUT"])
def update_car(id):
    data=request.json
    for c in range(len(cars)):
        if cars[c]["id"]==id:
            cars[c]=data
    return jsonify(cars)

# delet
@app.route("/cars/<int:id>",methods=["DELETE"])
def delete_car(id):
    for c in range(len(cars)):
        if cars[c]["id"]==id:
            cars.pop(c)
    return jsonify(cars)

app.run(port=8000)
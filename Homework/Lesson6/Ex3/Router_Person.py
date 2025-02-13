
from Persons_bl import Persons_Serviec
from flask import Blueprint, jsonify, request, abort

persons=Blueprint("persons",__name__)
persons_bl=Persons_Serviec()

@persons.route("/", methods=["GET"])
def get_all_persons():
    return jsonify(persons_bl.get_all_persons())

@persons.route("/<int:id>", methods=["GET"])
def get_person_by_id(id):
    return jsonify(persons_bl.get_by_id(id))

@persons.route("/", methods=["POST"])
def add_person():
    new_person=request.json
    return jsonify(persons_bl.add_person(new_person))

@persons.route("/<int:id>", methods=["PUT"])
def updata_person(id):
    new_person=request.json
    return jsonify(persons_bl.update_person(id,new_person))

@persons.route("/<int:id>", methods=["DELETE"])
def delete_person(id):
    return jsonify(persons_bl.delete_person(id))
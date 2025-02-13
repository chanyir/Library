
from BL.Student_Bl  import Students_service
from flask import Blueprint, jsonify, request

students=Blueprint("students",__name__)
students_bl=Students_service()

@students.route("/",methods=["GET"])
def get_all_students():
    return jsonify(students_bl.get_all_students()) 

@students.route("/<name>", methods=["GET"])
def get_by_name(name):
    return jsonify(students_bl.get_by_name(name))

@students.route("/", methods=["POST"])
def add_student():
    new_student=request.json
    return jsonify(students_bl.add_student(new_student))

@students.route("/<int:id>", methods=["PUT"])
def update_student(id):
    new_student=request.json
    return jsonify(students_bl.updata_student(id,new_student))

@students.route("/<int:id>", methods=["DELETE"])
def delete_student(id):
    return jsonify(students_bl.delete_student(id))
    
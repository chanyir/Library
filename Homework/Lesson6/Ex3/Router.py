
from User_Bl import MoviesServiec
from flask import Blueprint, jsonify, request, abort

movies=Blueprint("movies",__name__)
movies_bl=MoviesServiec()

@movies.route("/", methods=["GET"])
def get_all_movies():
    return jsonify(movies_bl.get_all_movies())





from flask import Flask
app = Flask(__name__)

from Router import movies 
from Router_Person import persons

app.register_blueprint(movies, url_prefix="/movies")
app.register_blueprint(persons, url_prefix="/persons")

app.run(port=8000)




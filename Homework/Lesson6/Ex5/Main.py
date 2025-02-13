
from bson import ObjectId
from flask import Flask
from flask.json.provider import DefaultJSONProvider
# from flask_cors import CORS
from RAUTERS.Student_Rauter import students
app = Flask(__name__)

# CORS(app)
class CustomJSONEncoder(DefaultJSONProvider):
    def __init__(self, app):
        super().__init__(app)
 
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(self, obj)
 
 
app.json = CustomJSONEncoder(app)

app.register_blueprint(students ,url_prefix="/students")

app.run(port=8000)

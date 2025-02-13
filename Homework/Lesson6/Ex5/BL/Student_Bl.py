from pymongo import MongoClient

class Students_service:
    def __init__(self):
        self.client=MongoClient(port=27017)
        self.db=self.client["KivunDB"]
        self.students_collection=self.db["students"]
    
    def get_all_students(self):
        return list(self.students_collection.find({})) 
    
    def get_by_name(self, name):
        return self.students_collection.find_one({"name": name}) 
    
    def updata_student(self,id,new_student):
        self.students_collection.update_one({"id": id},{"$set":new_student})
        return "updated"
    
    def delete_student(self, id):
        self.students_collection.delete_one({"id": id})
        return"delete"

    def add_student(self, new_student):
        self.students_collection.insert_one(new_student)
        return "created"

        
        
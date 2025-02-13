from pymongo import MongoClient
from Classes.Shelf import Shelf

client=MongoClient(port=27017)
db=client["KivunDB"]
Shelves_Collection=db["Shelves"]

def get_shelves():
    shelves=Shelves_Collection.find()
    shelves_list=[]
    for shelf in shelves:
        s=Shelf(shelf["books"])
        shelves_list.append(s)
    return list(shelves_list)

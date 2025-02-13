import json
from pymongo import MongoClient



client=MongoClient(port=27017)
db=client["KivunDB"]
movies_Collection=db["movies"]

# כתיבה לקובץ JSON 
# לא מיותר, לא רצינו שיכתוב שוב כל פעם כשמריצים.
# with open("../movies.json","r",encoding="utf-8")as file:
#     data=json.load(file)
#     map_data=list(map(lambda x:
#             { "id":x["id"],"name":x["name"],"genres":x["genres"],"averege rating":x["rating"]["average"] }
#                       ,data[:10]))
    
# movies_Collection.insert_many(map_data)
name_movies=input("press movies name\n")
update_name=input("press movies update_name\n")

movies_Collection.update_one({"name":name_movies},{"$set":{"name":update_name}})




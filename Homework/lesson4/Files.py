import json
import os
print(os.getcwd())

# ex1----------------

def Files_utils(nameStreet):
    with open(f"{os.getcwd()}\\Homework\\lesson4\\Person.json","r") as file:
        data=json.load(file)
    filtered=list(filter(lambda x : x["address"]["strit"]["name"]==nameStreet, data["persons"]))
    print(filtered)

# print(data)
Files_utils("nechemya")
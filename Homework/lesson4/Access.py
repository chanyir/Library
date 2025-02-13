import requests
import json

# ex2----------------------
USERS_URL="https://jsonplaceholder.typicode.com/users"
TODOS_URL="https://jsonplaceholder.typicode.com/todos?userId="



id=input("enter id user")
resp=requests.get(f"{USERS_URL}/{id}")
data=resp.json()
print(f"name:{data["name"]} email:{data["email"]}")

if data["name"][0]=='E':
    resp2=requests.get(f"{TODOS_URL}{id}")
    todo=resp2.json()
    todos=list(map(lambda x:x["title"],todo))
    with open("./titels.json","w")as file:
        json.dump(todos,file)


import requests
import json
USERS_URL="https://jsonplaceholder.typicode.com/users"

def get_user(name,email):
    res=requests.get(f"{USERS_URL}?name={name}&email={email}")
    data=res.json()
    return data
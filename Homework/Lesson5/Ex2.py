# import Build_Rest
import requests

id=int(input("press id\n"))
model=input("press model\n")
year=int(input("press year\n"))
driver_name=input("press driver_name\n")

car={"id":id,"model":model,"year":year,"driver":driver_name}

data=requests.post("http://localhost:8000/cars",json=car)

print(data.json())
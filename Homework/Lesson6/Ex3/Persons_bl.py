import json

class Persons_Serviec:
    def __init__(self):
        self.__persons=[
          {"id":1,"name":"chany","phone":"0533103377"},
          {"id":2,"name":"pniny","phone":"0533121240"},
          {"id":3,"name":"esty" ,"phone":"0583273293"}
        ]

    def get_all_persons(self):
        return list(map(lambda x: x["name"],self.__persons)) 
    
    def get_by_id(self,id): 
        return list(filter(lambda x: x["id"]==id,self.__persons)) 
    
    def update_person(self,id,person):
        for i in range(len(self.__persons)):
            if self.__persons[i]["id"]==id:
                self.__persons[i]=person
                break
        return self.__persons
    
    def add_person(self,person):
        return self.__persons.append(person)
    
    def delete_person(self,id):
        p=list(filter(lambda x:not x["id"]==id,self.__persons))
        self.__persons=p
        # for i in range(len(self.__persons)):
        #     if self.__persons[i]["id"]==id:
        #         self.__persons[i]=person
        #         break
        return self.__persons
        
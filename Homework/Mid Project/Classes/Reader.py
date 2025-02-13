

from datetime import datetime

class Reader:
    def __init__(self,id=0,name=""):
        self.id=id
        self.name=name    
        self.books=[]

    def read_book(self,title):
        self.books.append({"title":title,"date":datetime.now().date()})
   


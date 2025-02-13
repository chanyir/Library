from Classes.Book import Book
from Classes.Shelf import Shelf
from Classes.Reader import Reader

class Library:
    def __init__(self,shelves=[],readers=[]):
        self.shelves=shelves
        self.readers=readers

    def is_there_place_for_new_book(self,shelf):
            return shelf.is_full

    def add_new_book(self,new_book):
        for s in self.shelves:
             if self.is_there_place_for_new_book(s):
                  s.add_Book(new_book)
                  break
    
    def delete_book(self,book_title):
         for index in range(len(self.shelves)):
              print(f"before--------  {self.shelves[index]}")
              self.shelves[index]=list(filter(lambda x: not x.title==book_title,self.shelves[index].books))
              print(self.shelves[index])
              break
    
    def change_locations(self,title1,title2):
         print(self.shelves)
         index1=-1
         index2=-1
         s1=None
         s2=None
         for s in self.shelves:
             if  index1==-1:
                for b in range(len(s.books)):
                    if s.books[b].title==title1:
                        index1=b
                        s1=s
                        break
             if  index2==-1:
                for b in range(len(s.books)):
                    if s.books[b].title==title2:
                        index2=b
                        s2=s
                        break
             if not index1==-1 and not index2==-1:
                  break
        
         if s1 and s2:
            s1.books[index1], s2.books[index2] = s2.books[index2], s1.books[index1]
         
         
    def change_locations_in_same_shelf(self,snum,b1,b2):
        self.shelves[snum].replace_books(b1,b2)
       

    def order_all_books(self):
        for s in self.shelves:
            s.books=s.order_books()
    
    def register_reader(self,name,id):
        read=Reader(id,name)
        self.readers.append(read)

    def remove_reader(self,id):
        self.readers=list(filter(lambda x: x.id!=id,self.readers))
     
    def reader_read_book(self,name,title):
        reader=list(filter(lambda x: x.name==name,self.readers))[0]
        reader.read_book(title)

    def search_by_autho(self,name):
        arr=[]
        for s in self.shelves:
            arr.extend(list(filter(lambda x: x.author==name,s.books)))
        return arr
        

    def print_data_r(self):
         for s in self.readers:
           print("-----")
           print(s.name)
           for b in s.books:
               print(b.title)
           print("-----")            


        
    def print_data(self):
         for s in self.shelves:
           print("-----")
           for b in s.books:
               print(b.title)
           print("-----")            
    

               
             
# b1=Book("st","aa",800)
# b2=Book("pniny","bb",400)
# b3=Book("st","cc",600)
# b4=Book("st","dd",550)
# b5=Book("rachel","ee",500)
# sh1=Shelf([b1,b2])
# sh2=Shelf([b3,b4])
# sh3=Shelf([b5])
# raeder1=Reader(1,"chany")
# raeder2=Reader(2,"pniny")
# raeder3=Reader(3,"st")
# raeder4=Reader(4,"lea")
# raeder5=Reader(5,"rachel")
# raeder6=Reader(6,"rut")
# raeder7=Reader(7,"et")


# # lib=Library()
# lib=Library([sh1,sh2,sh3],[raeder1,raeder2,raeder3,raeder4,raeder5,raeder6,raeder7])
# lib.reader_read_book("chany","bb")
# lib.reader_read_book("lea","ee")
# lib.remove_reader("et")

# arr=lib.search_by_autho("st")
# for a in arr:
#     print (a.title)

# lib.print_data_r()
# lib.change_locations("bb","ee")
# lib.change_locations_in_same_shelf(1,0,1)
# lib.order_all_books()
# lib.print_data()

         
              
              
         




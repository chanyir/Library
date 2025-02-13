

class Shelf:
    def __init__(self,books=[]):
        self.books=books
        self.is_full=False

    def  add_Book(self,book):
         if len(self.book)<5:
             self.books.append(book) 
             self.is_full=False
         else:
             print("The shelf is full")
             self.is_full=True

    def replace_books(self,num1,num2):
        if self.books[num1] is None or self.books[num2] is None:
            print("location is empty")
        else:
            self.books[num1], self.books[num2] = self.books[num2], self.books[num1]
            
    def order_books(self):
         lst = sorted(self.books, key=lambda book: book["num_of_pages"])
         return lst





from Classes.Book import Book
from Classes.Library import Library
from Crud.Placeholder import get_user
from Crud.Shelves import get_shelves
from Classes.Reader import Reader
import json
import os

l=Library()
l.shelves=get_shelves()

def login():
    name=input("Enter your name\n")
    email=input("Enter your email\n")

    user=get_user(name,email)
    if len(user)==0:
        print("user not found")
        return False
    else:
        print(f"welcome {name}")
        return True

def menu():
    print()
    print("welcome to our library")    
    print("For adding a book - Press 1")   
    print("For deleting a book - Press 2")   
    print("For changing books locations - Press 3")   
    print("For registering a new reader - Press 4")   
    print("For removing a reader - Press 5")   
    print("For searching books by author - Press 6")   
    print("For reading a book by a reader - Press 7")   
    print("For ordering all books - Press 8")  
    print("For saving all data - Press 9")
    print("For loading data - Press 10")   
    print("For exit - Press 11")   

    chois=input("enter your chois: ")
    match (chois):
        case "1":
             add_book()
             menu()
        case "2":
            delete_book()
            menu()
        case "3":
            change_locations()
            menu()
        case "4":
           add_new_reader()
           menu()
        case "5":
           delete_reader()
           menu()
        case "6":
           searching_books_by_author()
           menu()
        case "7":
           book_by_reader()
           menu()
        case "8":
           ordering_all_books()
           menu()
        case "9":
           saving_all_data()
           menu()
        case "10":
           loading_data()
           menu()
        case "11":
            print("goodbye")
# case 1    
def add_book():
    title=input("Enter the title of the book")
    author=input("Enter the author of the book")
    num_of_pages=input("Enter the num_of_pages of the book")
    b=Book(title,author,num_of_pages)
    l.add_new_book(b)
    print("added successfully")

# case 2
def delete_book():
    title=input("Enter the title of the book")
    l.delete_book(title)
    print("deleted successfully")

# case 3
def change_locations():
    title1=input("Enter the first title of the book")
    title2=input("Enter the second title of the book")
    l.change_locations(title1,title2)
    print("chenged successfully")

# case 4   
def add_new_reader():
    name=input("Enter reader name")
    id=input("Enter reader id")
    l.register_reader(name,id)
    print("registered successfully")

# case 5
def delete_reader():
     id=input("Enter reader id")
     l.remove_reader(id)
     print("deleted successfully")

# case 6
def searching_books_by_author():
     name=input("Enter author name")
     l.search_by_autho(name)
     print(l.search_by_autho(name))
# case 7
def book_by_reader():
    name=input("Enter reader name")
    title=input("Enter title book")
    l.reader_read_book(name,title)
# case 8
def ordering_all_books():
    l.order_all_books()
# case 9
def saving_all_data():
    name_file=input("Enter reader name file")

    library_dic={"shelves":[vars(shelf)for shelf in l.shelves],"reders":[vars(reder) for reder in l.readers]}
    with open(f"./Files/{name_file}.json","w") as file:
        json.dump(library_dic,file)
# case 10
def loading_data():
    name_file=input("Enter reader name file")
    with open(f"./Files/{name_file}.json","r") as file:
        data=json.load(file)
    print(data)

log=login()
if log:
    menu()

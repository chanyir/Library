from Homework.lesson3.Object_oriented.Ex1.Toy import Toy
from Homework.lesson3.Object_oriented.Ex1.Ball import Ball

class Store:
    def __init__(self, toys=[]):
        self.toys=toys 

    def add_toy(self,toy):
        self.toys.append(toy)
        print("Added successfully")

    def Play_all_toys(self):
        for t in self.toys:
            t.play()


store=Store()
toy1=Toy(25,"red")
toy2=Toy(100,"blue")
toy3=Toy(50,"gteen")
Ball=Ball(30,"black",65,"pl")


store.add_toy(toy1)
store.add_toy(toy2)
store.add_toy(Ball)
        
store.Play_all_toys()


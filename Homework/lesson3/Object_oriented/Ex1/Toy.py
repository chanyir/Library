

class Toy:
    def __init__(self,price,color):
        if price>0:
            self.price=price
        else:
            print("Wrong price")
        self.color=color

    def play(self):
        print("playing the toy")

    def buy(self):
        print("buying the toy")



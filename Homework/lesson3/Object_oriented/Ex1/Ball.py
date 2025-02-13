from Homework.lesson3.Object_oriented.Ex1.Toy import Toy

class Ball(Toy):
    def __init__(self,price,color,radius,material):
        super().__init__(price,color)
        if radius>0:
            self.radius=radius
        else:
            print("Wrong radius")
        self.material=material

    def play(self):
        print("playing the ball")

    def buy(self):
        print("buying the ball")
   
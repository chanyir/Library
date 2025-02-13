from Animal import Animal
from Monkey import Monkey

class Chimpanzee(Monkey):
    def __init__(self,num_legs,height,color):
        super().__init__(num_legs,color)
        if height>=100:
            self.height=height
        else:
            print("Wrong height")


    def print_data(self):
        super().print_data()
        print(f"height:{self.height}") 
    
    
    


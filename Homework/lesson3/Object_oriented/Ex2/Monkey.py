from Animal import Animal

class Monkey(Animal):
    def __init__(self,num_legs,color):
        super().__init__(num_legs)
        self.color=color

    def print_data(self):
        super().print_data()
        print(f"color:{self.color}") 
    
    def eat(self):
        print("Monkey is eating")
    


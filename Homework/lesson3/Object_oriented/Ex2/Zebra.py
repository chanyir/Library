from Animal import Animal

class Zebra(Animal):
    def __init__(self,num_strips,num_legs):
        super().__init__(num_legs)
        if num_strips>0:
            self.num_strips=num_strips
        else:
            print("Wrong num_strips")

    def print_data(self):
        super().print_data()
        print(f"Num of strips:{self.num_strips}") 
    
    def eat(self):
        print("Zebra is eating")
    


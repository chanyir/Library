
class Animal:
    def __init__(self,num_legs ):
       self.num_legs=num_legs

    def eat(self):
        print("Animal is eating")

    def print_data(self):
        print(f"Num of legs{self.num_legs}")
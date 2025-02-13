from Animal import Animal
from Zebra import Zebra
from Monkey import Monkey
from Chimpanzee import Chimpanzee

class Zoo:
    def __init__(self,animals=[]):
        self.animals=animals

    def add_animal(self,animal):
        self.animals.append(animal)

    def Count_Animals(self):
        print(f"Ther are {len(self.animals)} animals in this zoo")
    
    def Feed(self):
        for a in self.animals:
            a.eat()

zoo=Zoo()
animal=Animal(6)
monkey=Monkey(2,"brown")
zebra=Zebra(4,25)
chimpanzee=Chimpanzee(2,160,"black")

zoo.add_animal(animal)
zoo.add_animal(monkey)
zoo.add_animal(zebra)
zoo.add_animal(chimpanzee)

zoo.Feed()

for a in zoo.animals:
    a.print_data()

      
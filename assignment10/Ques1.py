'''Ques 1. Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is
inheriting Animal and access the base class method.'''


class Animal:
    def animal_attribute(self):
        print("This is an Animal Class")
class mankey(Animal):
    def display(self):
        print("This is the mankey Class")

a=mankey()
a.animal_attribute()
a.display()















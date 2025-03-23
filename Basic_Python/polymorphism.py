from typing import List

class Animal:
    def sound(self): pass


class Dog(Animal):
    def sound(self):
        return "Woof Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow Meow!"
    
animals: List[Animal] = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())

from rich import print

class Engine:
    def start(self):
        print("Engine starts!")

    def stop(self):
        print("Engine stops!")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

car = Car()
car.start()
car.stop()

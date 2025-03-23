from rich import print

class LogMixin:
    def log(self, message: str) -> None:
        print(f'Log: {message}')

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        pass

class Dog(LogMixin, Animal):
    def speak(self):
        self.log(f'{self.name} says woof!')

dog = Dog('Buddy')
dog.speak()
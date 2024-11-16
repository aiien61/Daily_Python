from dataclasses import dataclass, FrozenInstanceError
from time import time

# Create class without dataclass
class NormalFruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    # __e1__ has to be defined if comparison is involved
    def __eq__(self, other):
        pass


banana = NormalFruit('Banana', 10)
apple = NormalFruit('Apple', 20)
banana2 = NormalFruit('Banana', 10)

print(apple)
print(banana == banana2)


# Create class with dataclass
@dataclass
class FastFruit:
    name: str
    calories: float = 10  # with default value


banana = FastFruit('Banana', 10)
apple = FastFruit('Apple', 20)
banana2 = FastFruit('Banana', 10)

print(banana)
print(banana == banana2)

banana.calories = 60
print(banana)

# Make the instances of the class not allowed to be changed
@dataclass(frozen=True)
class TropicalFruit:
    name: str
    calories: float = 10


try:
    banana = TropicalFruit('Banana', 10)
    banana.calories = 60
except FrozenInstanceError as e:
    print(e)
finally:
    print(banana)


# Make the instantiation of the class quicker if there are many instances to be made
@dataclass(slots=True)
class TaiwanFruit:
    # __slots__ = ['name', 'calories']  # same as slots=True in parameter in @dataclass
    name: str
    calories: float

start = time()
taiwanfruits = [TaiwanFruit('banana', 10) for _ in range(1_000_000)]
print(time() - start)

start = time()
taiwanfruits = [NormalFruit('apple', 10) for _ in range(1_000_000)]
print(time() - start)


# parameter keyword must be specified explicitly when creating an instance
@dataclass(kw_only=True)
class BigFruit:
    name: str
    calories: float

try:
    watermelon = BigFruit('Watermelon', 20)
    print(watermelon)
except TypeError as e:
    print(e)
    watermelon = BigFruit(name='Watermelon', calories=20)
    print(watermelon)


# Use dataclass to prevent unexpected typos
@dataclass(slots=True)
class Person:
    name: str
    age: int
    job: str = None
    friends: list[str] = None

    def __str__(self):
        return f'{self.name} is {self.age} years old and works as a {self.job}. Friends: {self.friends}'
    
json: dict = {
    'name': 'Bob',
    'age': 10,
    'job': 'Salesman',
    'friends': ['Mario', 'Luigi']
}

# intentional typo (name to be naem)
try:
    print(json['naem'])
except KeyError as e:
    print(e)


bob = Person(json['name'], json['age'], json['job'], json['friends'])
bob2 = Person(**json)
print(bob.job)
print(bob)
print(bob == bob2)

# dataclass with property
@dataclass
class Rectangle:
    width: float
    height: float

    @property
    def area(self) -> float:
        return self.width * self.height
    
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def describe(self) -> None:
        print(f'{self}')
        print(f'Area: {self.area}')
        print(f'Perimeter: {self.perimeter}')

rect1: Rectangle = Rectangle(width=10, height=20)
rect1.describe()
print(rect1.area)
rect1.height = 100
print(rect1.area)
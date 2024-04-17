# Variable reference
spam = 50
cheese = spam
spam = 100
print(spam)
print(cheese)

# list reference
spam = [i for i in range(6)]
cheese = spam
cheese[1] = 'Hello'
print(cheese)
print(spam)

# to pass by reference
def eggs(cheese):
    cheese.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam) # output [1,2,3,'Hello'] because passing the reference of spam into function eggs instead of its value

# use copy and deepcopy to pass by value
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 100
print(spam)
print(cheese)

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 100
print(spam)
print(cheese)

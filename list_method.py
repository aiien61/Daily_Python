import random

spam = ['cat', 'dog', 'horse', 'bunny']
print(f"list 'spam' consist of: {spam}")

# Get the index of a certain element in a list
try:
    index = spam.index('horse')
    print(f"The index of 'howdy' in the spam list: {index}")
    index = spam.index('elephant')
    print(f"The index of 'hey' in the spam list: {index}")
except ValueError as e:
    print("Can't find out the element in the list.", e)

# Append an element into the end of a list
spam.append('moose')
print(f'After adding a new element in the list: {spam}')

# Insert an element into a specific location in a list
spam.insert(1, 'elephant')
print(f'After inserting a new element in the 1st place of the list: {spam}')

# Remove a value from a list
spam.remove('bunny')
print(f"After removing 'bunny' from the list: {spam}")

del spam[3]
print(f"After removing the 3rd element in the list: {spam}")

# Sorting all the values in a list in place
spam = [random.randint(1, 10) for _ in range(5)]
print(f"A new unsorted list: {spam}")
spam.sort()
print(f"After sorting in ascending order: {spam}")
spam.sort(reverse=True)
print(f"After sorting in descending order: {spam}")

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
print(f"A new characters list: {spam}")
spam.sort() # sort by ASCII order
print(f"After sorting in ASCII order: {spam}")
spam.sort(key=str.lower) # convert all the elements into lowercase, then sort.
print(f"After sorting in alphabetical order: {spam}")

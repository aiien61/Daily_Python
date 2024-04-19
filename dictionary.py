import pprint

def birthday():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    while True:
        name = input('Enter a name (blank to quit): ')

        if not name:
            break

        if name in birthdays:
            print(f"{birthdays[name]} is the birthday of {name}")
        else:
            print(f"I do not have birthday information of {name}")
            birthdays[name] = input('What is their birthday?')
            print('Birthday database updated.')
    return None

spam = {5: 'this', 2: 'is', 1: 'a', 30: 'book'}

# Get keys
print(spam.keys())

# Get values
print(spam.values())

# Get key-value pairs
print(spam.items())

# Get value with personalised default value
print(spam.get(2, 'no key found'))
print(spam.get(12, 'no key found'))

# Set default value initially if key is not found in a dictionary
spam = {'name': 'Zoopia', 'genre': 'anime'}
spam.setdefault('language', 'English')
print(spam)
print(spam.get('language', 'Japanese'))


def character_count():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}

    for char in message.upper():
        count.setdefault(char, 0)
        count[char] += 1
    
    pprint.pprint(count)


character_count()

all_guests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}

def totoal_brought(guests: dict, item: str) -> int:
    num_brought = 0
    for guest_item in guests.values():
        num_brought += guest_item.get(item, 0)
    return num_brought

print('Number of things being brought:')
for item in ['apples', 'cups', 'cakes', 'ham sandwiches', 'apple pies']:
    print(f"- {item.capitalize()}  {totoal_brought(all_guests, item)}")

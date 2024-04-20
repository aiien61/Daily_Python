# raw string
print('This is a Carol\'s cat.')
print(r'This is a Carol\'s cat.')

# upper() & lower()
spam = 'Hello world'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

# title() & capitalize()
spam = spam.capitalize()
print(spam)
spam = spam.title()
print(spam)

# isupper() & islower()
spam = 'Hello world'
print(spam.islower())  # false
print(spam.isupper())  # false
print('HELLO'.isupper())  # true
print('world'.islower())  # true
print('abc12345'.islower())  # true
print('ABC12345'.isupper())  # true
print('12345'.islower())  # false
print('12345'.isupper())  # false

# isalpha(): whether letters only
print('hello'.isalpha())  # true
print('hello123'.isalpha())  # false

# isalnum(): whether letters or number is contained only
print('abc123'.isalnum())  # true
print('123'.isalnum())  # true
print('abc'.isalnum())  # true

# isdecimal(): whether numbers only
print('123'.isdecimal())  # true
print('abc'.isdecimal())  # false
print('abc123'.isdecimal())  # false


# isspace(): whether whitespace only
print('   '.isspace())  # true
print('  abc   '.isspace())  # false

# istitle(): whether titlecase only
print('This Is Title Case'.istitle())  # true
print('This Is Title Case 123'.istitle())  # true
print('This Is not Title Case'.istitle())  # false
print('This Is Also NOT Title Case'.istitle())  # false

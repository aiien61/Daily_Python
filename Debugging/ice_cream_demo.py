from icecream import ic

def calculate_discount(price: float, discount_rate: float):
    discount: float = price * discount_rate / 100
    final_price: float = price - discount
    ic(price, discount_rate, discount, final_price)
    return final_price

calculate_discount(100, 10)

# ---
nested_data: dict = {'josh': {'countries': ['thailand', 'vietnam', 'france']},
                     'bob': {'countries': ['canada']}}

ic(nested_data)

# ---
def validate_data(data):
    from icecream import ic
    ic.disable() # turn on if no need to print out the debugging message

    if not data:
        ic('Data is missing!')
        return False
    if 'name' not in data:
        ic('Missing name')
        return False
    if not data.get('age') or data['age'] <= 0:
        ic('Invalid age:', data['age'])
        return False
    ic('Data is valid')
    return True


validate_data({'name': 'Theodore III', 'age': -55})
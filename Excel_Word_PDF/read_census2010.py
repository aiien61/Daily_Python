import os
import census2010

anchorage_data = census2010.all_data['AK']['Anchorage']
print(anchorage_data)

anchorage_population = anchorage_data['population']
print(f'The 2010 populatino of Anchorage was {anchorage_population}')
